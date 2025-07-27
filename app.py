# app.py
from gradio_client import Client
from flask import Flask, request, jsonify

app = Flask(__name__)
client = Client("asmaaabd0/cv-suggester")

@app.route("/generate_cv", methods=["POST"])
def generate_cv():
    data = request.json
    result = client.predict(
        name=data["name"],
        age=data["age"],
        job_title=data["job_title"],
        skills_input=data["skills_input"],
        cv_input=data["cv_input"],
        api_name="/generate_cv_and_skills"
    )
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
