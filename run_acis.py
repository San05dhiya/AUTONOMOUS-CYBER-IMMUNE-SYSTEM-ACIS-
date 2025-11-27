# ===================================
# ACIS - MAIN EXECUTION ENGINE
# ===================================
import time
from acis_agent import monitor_system
from anomaly_model import detect_anomaly
from antibody_generator import generate_antibody
from response_engine import respond_to_threat

print("\n=== AUTONOMOUS CYBER IMMUNE SYSTEM STARTED ===")

try:
    while True:
        metrics = monitor_system()
        anomaly = detect_anomaly(metrics)

        if anomaly:
            print("\n[ACIS] ⚠ Anomaly Detected!")
            respond_to_threat()
            generate_antibody(metrics)
        else:
            print("[ACIS] System Normal ✓")

        time.sleep(3)
except KeyboardInterrupt:
    print("\n[ACIS] Stopped by user.")
