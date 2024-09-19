# WhoWeB Scanner

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple website scanner tool to gather basic information.

## Features

- Extracts links from a webpage.
- Detects cookies.
- Retrieves website IP address and associated country.
- Finds email addresses (if present in mailto links).
- Checks for Apache server and PHP usage.
- Identifies the presence of Google Analytics.
- Detects frames.
- Lists uncommon HTTP headers.
- Displays page title and number of meta tags.

## Installation

1. Make sure you have Python 3.x installed.
2. Install the required libraries:

   ```bash
   pip install requests beautifulsoup4 colorama
   ```
   ```bash
   python whoweb_scanner.py [URL]
   ```
## Disclaimer
This tool is intended for educational and informational purposes only. Use it responsibly and respect the terms of service of the websites you scan.

   
   
