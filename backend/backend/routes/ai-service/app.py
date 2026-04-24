from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Service Running"

@app.route("/analyze")
def analyze():
    return jsonify({
        "feedback": ["Keep your back straight"]
    })
