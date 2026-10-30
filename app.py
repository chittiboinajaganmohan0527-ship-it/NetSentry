from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>NetSentry Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            background: #101827;
            color: white;
            font-family: Arial;
            padding: 30px;
        }
        .card {
            background: #1e293b;
            padding: 20px;
            margin: 15px 0;
            border-radius: 12px;
        }
        h1 { color: #60a5fa; }
    </style>
</head>
<body>
    <h1>NetSentry</h1>
    <h3>Network Intrusion Detection and Alert System</h3>

    <div class="card">
        <h2>Network Monitoring Dashboard</h2>
        <p>System Status: Ready</p>
        <p>Client-Server Network: Not connected yet</p>
        <p>Detection Algorithm: Under development</p>
        <p>Total Events: 0</p>
        <p>Security Alerts: 0</p>
    </div>

    <div class="card">
        <h2>Project Features</h2>
        <p>TCP Client-Server Communication</p>
        <p>Rule-Based Anomaly Detection</p>
        <p>Network Event Monitoring</p>
        <p>SQLite Event Storage</p>
    </div>
</body>
</html>
"""

@app.route("/")
def dashboard():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)