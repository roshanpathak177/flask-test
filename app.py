from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Hello, World!"

@app.route("/mbsa")
def mbsa():
  return render_template("index.html")


