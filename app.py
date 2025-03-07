from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.json
    text = data.get("text", "")
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    
    return jsonify({"summary": summary[0]["summary_text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Summarizer Backend is Running!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to port 10000
    app.run(host="0.0.0.0", port=port)
