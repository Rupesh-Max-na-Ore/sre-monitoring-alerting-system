import time

from flask import Flask
from prometheus_client import Summary, start_http_server

app = Flask(__name__)

# Metric: request latency
REQUEST_TIME = Summary("request_processing_seconds", "Time spent processing request")


@app.route("/")
@REQUEST_TIME.time()
def home():
    time.sleep(0.3)  # simulate latency
    return "Hello SRE Monitoring"


if __name__ == "__main__":
    # Expose metrics on port 8000
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
