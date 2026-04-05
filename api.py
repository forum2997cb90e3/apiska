from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://admin:123456qwerty@cluster0.mvdyb6h.mongodb.net/?appName=Cluster0")
db = client["bot"]

logs = db["logs"]
bans = db["bans"]

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

@app.route("/bans")
def get_bans():
    data = []

    for ban in bans.find().sort("user_id", 1):
        data.append({
            "user_id": str(ban.get("user_id")),
            "reason": ban.get("reason")
        })
    
    return jsonify(data)
    
if __name__ == "__main__":
    app.run()