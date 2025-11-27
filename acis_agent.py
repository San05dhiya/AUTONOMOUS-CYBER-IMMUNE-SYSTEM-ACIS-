# ================================
# ACIS - HOST SENSOR AGENT
# ================================
import psutil
import time
import json

def collect_metrics():
    data = {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "process_count": len(psutil.pids()),
        "network_connections": len(psutil.net_connections())
    }
    return data

def monitor_system():
    metrics = collect_metrics()
    print("[AGENT] Metrics:", metrics)
    return metrics

if __name__ == "__main__":
    while True:
        monitor_system()
        time.sleep(2)
