from datetime import datetime

# Rule-based intrusion detection system

MAX_CONNECTION_ATTEMPTS = 10
MAX_REQUESTS = 20

def detect_anomaly(event):
    """
    Analyze network events and identify suspicious activity.
    """

    alerts = []

    source_ip = event.get("source_ip", "Unknown")
    event_type = event.get("event_type", "")
    details = event.get("details", {})

    if isinstance(details, str):
        details = {"message": details}

    attempts = details.get("attempts", 0)
    requests = details.get("requests", 0)

    # Rule 1: Detect excessive connection attempts
    if attempts > MAX_CONNECTION_ATTEMPTS:
        alerts.append({
            "source_ip": source_ip,
            "alert_type": "Brute Force Attack",
            "description": "Too many connection attempts detected"
        })

    # Rule 2: Detect excessive network requests
    if requests > MAX_REQUESTS:
        alerts.append({
            "source_ip": source_ip,
            "alert_type": "High Traffic",
            "description": "Unusual number of network requests detected"
        })

    # Rule 3: Detect suspicious event types
    suspicious_events = [
        "port_scan",
        "unauthorized_access",
        "malicious_login"
    ]

    if event_type.lower() in suspicious_events:
        alerts.append({
            "source_ip": source_ip,
            "alert_type": "Suspicious Activity",
            "description": f"Suspicious event detected: {event_type}"
        })

    return alerts


def analyze_event(event):
    alerts = detect_anomaly(event)

    if alerts:
        return "Suspicious", alerts

    return "Normal", []