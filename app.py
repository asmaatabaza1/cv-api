import os
from gradio_client import Client
from flask import Flask, request, jsonify

app = Flask(__name__)
client = Client("asmaaabd0/cv-suggester")

@app.route("/generate_cv", methods=["POST"])
def generate_cv():
    data = request.json or {}
    name = data.get("name", "")
    age = data.get("age", "")
    job_title = data.get("job_title", "")
    skills_input = data.get("skills_input", "")
    cv_input = data.get("cv_input", "")

    try:
        result = client.predict(
            name=name,
            age=age,
            job_title=job_title,
            skills_input=skills_input,
            cv_input=cv_input,
            api_name="/generate_cv_and_skills"
        )
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
