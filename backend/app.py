"""
FedCollect AI - Backend Skeleton
Prototype-level API structure for hackathon submission
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "FedCollect AI backend is running",
        "status": "prototype"
    })

@app.route("/health")
def health_check():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
