import subprocess

def enable_monitor(interface):
    try:
        cmd = f"airmon-ng start {interface}"
        return subprocess.getoutput(cmd)
    except Exception as e:
        return f"[ERROR] {e}"

def scan_networks():
    try:
        cmd = "airodump-ng wlan0mon"
        return subprocess.getoutput(cmd)
    except Exception as e:
        return f"[ERROR] {e}"

def evil_twin(ssid):
    return "[INFO] Evil Twin setup requires additional config (hostapd + dnsmasq)."
