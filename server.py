import socket
import json
from datetime import datetime

from detection import analyze_event
from database import create_database, save_event, save_alert

HOST = "0.0.0.0"
PORT = 9999


def start_server():

    create_database()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(5)

    print("================================")
    print("     NetSentry Server Started")
    print("     Listening on port 9999")
    print("================================")

    while True:

        conn, addr = server.accept()

        with conn:

            print("Client connected:", addr)

            try:
                data = conn.recv(4096)

                if not data:
                    continue

                event = json.loads(data.decode("utf-8"))

                if not isinstance(event, dict):
                    raise ValueError("Event must be a JSON object")

                if not all(key in event for key in
                           ["source_ip", "event_type", "details"]):
                    raise ValueError("Missing required event fields")

                if not isinstance(event["details"], dict):
                    raise ValueError("Details must be a JSON object")

                timestamp = datetime.now().isoformat()

                status, alerts = analyze_event(event)

                save_event(
                    timestamp,
                    event["source_ip"],
                    event["event_type"],
                    json.dumps(event["details"]),
                    status
                )

                for alert in alerts:
                    save_alert(
                        timestamp,
                        alert["source_ip"],
                        alert["alert_type"],
                        alert["description"]
                    )

                response = {
                    "status": "success",
                    "detection_status": status,
                    "alerts": alerts
                }

                print("Received event:", event)
                print("Detection result:", status)
                print("Alerts:", alerts)

            except (ValueError, KeyError, json.JSONDecodeError) as error:

                response = {
                    "status": "error",
                    "message": str(error)
                }

            except Exception as error:

                response = {
                    "status": "error",
                    "message": str(error)
                }

            conn.sendall(json.dumps(response).encode("utf-8"))


if __name__ == "__main__":
    start_server()