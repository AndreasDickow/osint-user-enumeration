
# Project Title: Nextcloud User Enumeration OSINT - Proof of Concept

## Overview
This repository contains a proof of concept (PoC) for Brute Force Enumeration OSINT tested on  Nextcloud/OwnCloud instances. This project is designed for educational purposes to demonstrate how a brute force enumeration attack can be executed to uncover sensitive information. It should be used responsibly and only in environments where you have explicit permission to test.

## Description
This PoC illustrates how a list based brute force attack can be implemented using Python, showcasing the potential vulnerabilities within systems that do not implement adequate rate limiting or input validation mechanisms. The proposed mechanism targets country based surname lists as user account names.

## Features
- **Enumeration Script**: The core script that performs the brute force enumeration, attempting various combinations until the correct one is found.
- **Parallel Processing**: Utilizes Python's `concurrent.futures` module to demonstrate how parallel processing can expedite a brute force attack.
- **Session Management**: Implements `requests.Session` to optimize network requests during the enumeration process.
- **Result Analysis**: Includes functionality to analyze and segregate successful and unsuccessful attempts, providing insights into the attack's effectiveness.

## Prerequisites
- Python 3.x

## Installation
Clone this repository to your local machine using:
```
git clone https://github.com/AndreasDickow/osint-user-enumeration.git
git submodule update --init --recursive
cd osint-user-enumeration
pip install -r requirements.txt
```

## Usage
To run the enumeration scan script, execute the following command:
```
python scan.oy <domain> <comma separated country code targets>
e.g.
python scan.py example.tld de,at,gr
```

**Note:** Modify the script parameters as necessary to suit your testing environment or use case.

## Warning
This tool is intended for security research and educational purposes only. Unauthorized testing of websites, networks, or systems without explicit permission is illegal and unethical.

## Contributing
Contributions to this project are welcome! Please fork the repository, make your changes, and submit a pull request.

## License
This project is released under the [MIT License](LICENSE).

## Disclaimer
The authors of this project are not responsible for any misuse or damage caused by this tool. Users are urged to use this PoC responsibly and ethically, adhering to applicable laws and regulations.
