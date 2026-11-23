from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my Website" "<h1>HAHAHAHA<h1/>" # You wnt to use 'html' to write in your website cause you can add images font stiles and header types etc.

app.run(host="0.0.0.0")