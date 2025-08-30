from flask import Flask, render_template, jsonify, request
import os
from datetime import datetime

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "New Era Class 24")
APP_ENV = os.getenv("APP_ENV", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

@app.route("/")
def index():
    return render_template(
        "index.html",
        app_name=APP_NAME,
        app_env=APP_ENV,
        log_level=LOG_LEVEL,
    )

@app.route("/status")
def status():
    return jsonify(
        name=APP_NAME,
        env=APP_ENV,
        log_level=LOG_LEVEL,
        time=datetime.utcnow().isoformat() + "Z",
        container_id=os.uname().nodename if hasattr(os, "uname") else "unknown",
    )

@app.route("/echo")
def echo():
    msg = request.args.get("msg", "hello")
    return jsonify(echo=msg)

if __name__ == "__main__":
    # Dev server (use gunicorn in Docker)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)), debug=True)
