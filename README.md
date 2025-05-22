# Wi-Fi Risk Scanner

A simple Python tool to scan nearby public Wi-Fi networks, analyze their security types, and check known vulnerabilities from public databases. It warns you if any network is risky or known for attacks.

Perfect for digital nomads, travelers, and anyone concerned about Wi-Fi security.

---

## Features

- Scan nearby Wi-Fi SSIDs without needing a password or special adapter  
- Detect security protocols (WEP, WPA, WPA2, Open, etc.)  
- Cross-reference with known vulnerability databases (e.g., CVEs)  
- Highlight risky networks to avoid potential attacks  
- Export scan results to a CSV file  

---

## Installation

Make sure you have **Python 3.8+** installed.

```bash
git clone https://github.com/z3usx01/NetPatrol.git
cd NetPatrol
pip install -r requirements.txt
