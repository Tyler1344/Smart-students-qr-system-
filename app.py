
from flask import Flask, render_template
import json

app = Flask(__name__)

with open("students.json") as f:
    students = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student/<id>")
def student(id):
    student = students.get(id)
    return render_template("student.html", student=student)

if __name__ == "__main__":
    app.run(debug=True)