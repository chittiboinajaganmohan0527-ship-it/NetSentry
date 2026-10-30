import sqlite3

DB_NAME = "netsentry.db"


def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source_ip TEXT,
            event_type TEXT,
            details TEXT,
            status TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            source_ip TEXT,
            alert_type TEXT,
            description TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_event(timestamp, source_ip, event_type, details, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO events
        (timestamp, source_ip, event_type, details, status)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, source_ip, event_type, details, status))

    conn.commit()
    conn.close()


def save_alert(timestamp, source_ip, alert_type, description):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO alerts
        (timestamp, source_ip, alert_type, description)
        VALUES (?, ?, ?, ?)
    """, (timestamp, source_ip, alert_type, description))

    conn.commit()
    conn.close()


def get_events():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM events ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data


def get_alerts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alerts ORDER BY id DESC")
    data = cursor.fetchall()

    conn.close()
    return data