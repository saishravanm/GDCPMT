from flask import Flask
#! C:\xampp\htdocs\TPBase\venv\Scripts\python.exe
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!<p>"