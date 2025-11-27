# ===================================
# RESPONSE ENGINE
# ===================================
import psutil
import subprocess
import platform
import time

def isolate_network():
    # Simulation only: show message. Real isolation requires admin and careful commands.
    print("[RESPONSE] Network isolation triggered (simulation).")
    # Example real command (Linux): subprocess.run(["sudo","ip","link","set","eth0","down"])
    # On Windows real isolation would require disabling adapters via netsh (admin).

def kill_suspicious():
    killed = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name'] or ""
            # Example rule: if process name contains 'unknown' or suspicious pattern
            if "unknown" in name.lower() or "suspicious" in name.lower():
                proc.kill()
                killed.append(name)
                print("[RESPONSE] Suspicious process terminated:", name)
        except Exception:
            pass
    if not killed:
        print("[RESPONSE] No suspicious processes found by simple rule.")

def respond_to_threat():
    print("[RESPONSE] 🚨 Threat Detected!")
    isolate_network()
    kill_suspicious()
    # small wait to simulate actions
    time.sleep(1)
