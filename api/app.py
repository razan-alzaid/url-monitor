from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(os.environ.get("MONGO_URI"))
db = client.monitor
collection = db.urls

# 👇 هذا هو الداشبورد الآن
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/add", methods=["POST"])
def add_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL required"}), 400

    collection.insert_one({
        "url": url,
        "status": "unknown",
        "response_time": None
    })

    return jsonify({"message": "URL added"}), 201

@app.route("/urls", methods=["GET"])
def get_urls():
    urls = list(collection.find({}, {"_id": 0}))
    return jsonify(urls)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)