from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://admin:123456qwerty@cluster0.mvdyb6h.mongodb.net/?appName=Cluster0")
db = client["bot"]

logs = db["logs"]

@app.route("/")
def home():
    return "API WORK SUCCESSFULLY"

@app.route("/logs")
def get_logs():
    data = []

    for log in logs.find().sort("time", -1):
        data.append({
            "admin_id": str(log.get("admin_id")),
            "admin_username": log.get("admin_username"),
            "action": log.get("action"),
            "target_id": str(log.get("target_id")),
            "target_username": log.get("target_username"),
            "time": log.get("time")
        })

    return jsonify(data)
    
if __name__ == "__main__":
    app.run()