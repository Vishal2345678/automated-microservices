from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__, template_folder=".")


BACKEND_URL = "http://backend-service:5000"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/status")
def backend_status():
    try:
        response = requests.get(
            f"{BACKEND_URL}/health",
            timeout=3
        )

        if response.status_code == 200:
            return jsonify({
                "backend": "healthy",
                "message": "Backend service is operational"
            })

        return jsonify({
            "backend": "unhealthy",
            "message": "Backend returned an unexpected response"
        }), 503

    except requests.RequestException:
        return jsonify({
            "backend": "offline",
            "message": "Backend service is unreachable"
        }), 503


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )