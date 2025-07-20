import subprocess

def whois_lookup(domain):
    try:
        cmd = f"whois {domain}"
        result = subprocess.getoutput(cmd)
        return result
    except Exception as e:
        return f"[ERROR] {e}"

def nmap_scan(target):
    try:
        cmd = f"nmap -A {target}"
        result = subprocess.getoutput(cmd)
        return result
    except Exception as e:
        return f"[ERROR] {e}"
