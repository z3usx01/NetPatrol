Wi-Fi Risk Scanner
A simple Python tool to scan nearby public Wi-Fi networks, analyze their security types, and check known vulnerabilities from public databases. It warns you if any network is risky or known for attacks.

Perfect for digital nomads, travelers, and anyone concerned about Wi-Fi security.

Features
Scan nearby Wi-Fi SSIDs without needing a password or special adapter

Detect security protocols (WEP, WPA, WPA2, Open, etc.)

Cross-reference with known vulnerability databases (e.g., CVEs)

Highlight risky networks to avoid potential attacks

Export scan results to a CSV file

Installation
Make sure you have Python 3.8+ installed.


git clone https://github.com/z3usx01/NetPatrol.git
cd NetPatrol
pip install -r requirements.txt
Usage

python wifi_scanner.py
The program will scan available Wi-Fi networks and display their security info and risk status. Results will be saved to wifi_scan_results.csv.

How It Works
Scans nearby Wi-Fi networks using system Wi-Fi commands

Identifies security protocols for each network

Checks known vulnerabilities from public CVE databases or other sources

Marks networks with potential security issues as risky

Contributing
Contributions, issues, and feature requests are welcome!
Feel free to check issues page.

License
This project is licensed under the MIT License — see the LICENSE file for details.

Disclaimer
This tool is for educational purposes and personal use only.
Use it responsibly and do not attempt unauthorized access to networks.

