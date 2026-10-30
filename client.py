import socket
import json
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9999

test_events = [
    {
        "source_ip": "192.168.1.10",
        "event_type": "normal_traffic",
        "count": 10
    },
    {
        "source_ip": "192.168.1.20",
        "event_type": "failed_login",
        "count": 15
    },
    {
        "source_ip": "192.168.1.30",
        "event_type": "port_scan",
        "count": 100
    },
    {
        "source_ip": "192.168.1.40",
        "event_type": "normal_traffic",
        "count": 5
    }
]


def send_event(event):
    try:
        client = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        client.connect((SERVER_HOST, SERVER_PORT))

        message = json.dumps(event)
        client.sendall(message.encode("utf-8"))

        response = client.recv(4096)
        print("Sent event:", event)
        print("Server response:", response.decode("utf-8"))

        client.close()

    except ConnectionRefusedError:
        print("Error: Server is not running!")
    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    print("NetSentry Client Started")

    for event in test_events:
        send_event(event)
        time.sleep(1)

    print("All test events sent.")