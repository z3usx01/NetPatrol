import subprocess
import re
from colorama import init, Fore
import csv

init(autoreset=True)

def scan_wifi(interface='wlan0'):
    try:
        scan_result = subprocess.run(['sudo', 'iwlist', interface, 'scan'], capture_output=True, text=True, timeout=30)
        return scan_result.stdout
    except Exception as e:
        print(f"Scan error: {e}")
        return None

def parse_scan(output):
    networks = []
    for cell in output.split('Cell ')[1:]:
        ssid = re.search(r'ESSID:"([^"]+)"', cell)
        if not ssid:
            continue
        ssid = ssid.group(1)

        encryption = 'Open'
        if 'Encryption key:on' in cell:
            if 'WPA2' in cell:
                encryption = 'WPA2'
            elif 'WPA' in cell:
                encryption = 'WPA'
            elif 'WEP' in cell:
                encryption = 'WEP'
            else:
                encryption = 'Unknown'

        signal = re.search(r'Signal level=(-?\d+) dBm', cell)
        signal = int(signal.group(1)) if signal else None

        networks.append({'ssid': ssid, 'encryption': encryption, 'signal': signal})
    return networks

def classify_risk(enc):
    if enc.lower() == 'open':
        return 'HIGH', Fore.RED
    if enc.lower() == 'wep':
        return 'MEDIUM', Fore.YELLOW
    return 'LOW', Fore.GREEN

def main(interface='wlan0'):
    output = scan_wifi(interface)
    if not output:
        print("No Wi-Fi scan output. Exiting.")
        return

    networks = parse_scan(output)
    print(f"{'SSID':30} {'Encryption':10} {'Signal(dBm)':12} Risk")
    print('-'*65)
    for net in networks:
        risk, color = classify_risk(net['encryption'])
        signal = net['signal'] if net['signal'] is not None else 'N/A'
        print(f"{net['ssid'][:29]:30} {net['encryption']:10} {signal:<12} {color}{risk}")

    # Save results to CSV
    with open('wifi_scan_results.csv', 'w', newline='') as csvfile:
        fieldnames = ['SSID', 'Encryption', 'Signal(dBm)', 'Risk']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for net in networks:
            risk, _ = classify_risk(net['encryption'])
            writer.writerow({'SSID': net['ssid'], 'Encryption': net['encryption'], 'Signal(dBm)': net['signal'], 'Risk': risk})
    print("\nResults saved to wifi_scan_results.csv")

if __name__ == '__main__':
    main()
