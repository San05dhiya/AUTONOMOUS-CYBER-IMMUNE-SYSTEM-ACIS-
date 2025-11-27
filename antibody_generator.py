# ===================================
# ANTIBODY GENERATOR
# ===================================
import time
import json
import os

def generate_antibody(metrics):
    antibody = {
        "timestamp": time.ctime(),
        "rule": "BLOCK_HIGH_RISK_ACTIVITY",
        "details": metrics
    }

    # Save antibody to a file for demo / sharing
    fname = "antibody_" + str(int(time.time())) + ".json"
    with open(fname, "w") as f:
        f.write(json.dumps(antibody, indent=2))
    print("\n[IMMUNE SYSTEM] Antibody Generated and saved to", fname)
    print(json.dumps(antibody, indent=2))
    return antibody
