import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from AI_Assistant import AI_Assistant

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
assistant = AI_Assistant(api_key)

@app.get("/")
def home() :
    return(render_template("index.html"))

@app.post("/ask")
def ask() :
    question = request.form.get("question")
    response = assistant.answer_query(question)
    return jsonify({"response" : response}), 200

@app.post("/summarize")
def summarize() :
    email = request.form.get("email")
    response = assistant.summarize_email(email)
    return jsonify({"response" : response}), 200

if __name__ == "__main__" :
    app.run(debug=True)

