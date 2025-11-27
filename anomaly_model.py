# ===================================
# SIMPLE RULE-BASED ANOMALY DETECTOR
# ===================================
def detect_anomaly(metrics):
    score = 0

    if metrics["cpu"] > 80:
        score += 1
    if metrics["memory"] > 85:
        score += 1
    if metrics["process_count"] > 250:
        score += 1
    if metrics["network_connections"] > 100:
        score += 1

    if score >= 2:
        return True
    return False
