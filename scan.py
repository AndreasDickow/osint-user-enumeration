import os
import requests
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
import numpy as np

import argparse

parser=argparse.ArgumentParser(
    description='''Please provide separated country shortcodes like en,cn,dk''',
    epilog="""Let's go.""")
parser.add_argument('target', help=', provide a target domain like https://example.com')
parser.add_argument('countries', default=['gr,es'], help=', sperated country short codes like cn,hk')
args=parser.parse_args()
countries_list = args.countries
target = args.target
if not target.startswith('https://') and not target.startswith('http://'):
    target = 'https://' + target

base_path = 'Surnames/withoutStatistics'


def fetch_head_request(session, url):
    try:
        response = session.head(url)
        return url, int(response.headers.get('Content-Length', 0))
    except Exception as e:
        print(f"Error during request to {url}: {e}")
        return url, 0

def process_file(filename, session):
    results = []
    file_path = os.path.join(base_path, filename)

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]

    urls = [f"{target}/u/{urllib.parse.quote(line)}" for line in lines]

    with ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(fetch_head_request, session, url): url for url in urls}
        for future in as_completed(future_to_url):
            url, length = future.result()
            if length:
                results.append((url, length))

    return results

def detect_outliers(file_results):
    content_lengths = [length for _, length in file_results]

    Q1, median, Q3 = np.percentile(content_lengths, [25, 50, 75])
    IQR = Q3 - Q1
    upper_bound = Q3 + 5 * IQR

    outliers = [item for item in file_results if item[1] > upper_bound]

    return median, outliers

results_filename = "hits.txt"
with requests.Session() as session:
    for filename in os.listdir(base_path):
        country, ending = filename.split(".")
        if country in countries_list:
            print(f"Processing {filename}...")
            file_results = process_file(filename, session)
            if file_results:
                median, hit_list = detect_outliers(file_results)
                if len(hit_list) > 0:
                    with open(results_filename, 'a', encoding='utf-8') as f:
                        for line, length in hit_list:
                            print(f"Hit on {line}")
                            f.write(f"{line}\n")
                    print(f"results saved to {results_filename}.")
                else:
                    print(f"No hits found for {country}.")
            else:
                print(f"No data available for {country}.")
