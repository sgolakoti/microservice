from flask import Flask
import requests

app = Flask(__name__)

@app.route("/a")
def a():
    try:
        response = requests.get("http://service-a")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error contacting service-a: {e}", 500

@app.route("/b")
def b():
    try:
        response = requests.get("http://service-b")
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error contacting service-b: {e}", 500

if __name__ == "__main__":
    # Listen on all interfaces, port 8080
    app.run(host="0.0.0.0", port=8080)