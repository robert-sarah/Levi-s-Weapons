import subprocess
import os

def run_command(cmd):
    try:
        return subprocess.getoutput(cmd)
    except Exception as e:
        return f"[ERROR] {e}"

def check_root():
    if os.geteuid() != 0:
        return False
    return True
