from flask import Flask, jsonify
import os

app = Flask(__name__)


file_lines = []
file_path = './readme.txt'
if os.path.exists(file_path):
    with open('./files/readme.txt', 'r') as file:
        for line in file.readlines():
            file_lines.append(line)
else:
    file_lines.append("Could not find {}".format(file_path))


week_day = os.getenv("WEEK_DAY", "DEFAULT_WEEK")
weather_month = os.getenv("WEATHER_MONTH", "DEFAULT_MONTH")
weather = os.getenv("WEATHER", "DEFAULT_WEATHER")

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is my EX288 practice flask app!</p>"

@app.route("/configmap")
def read_configmap():
    return "<p>It's {} today, unusually for {} the weather is {}</p>".format(week_day, weather_month, weather)

@app.route("/filereader")
def read_file():
    return jsonify(file_lines)

@app.route("/flask-healthz")
def return_healthy():
    return "application healthy", 200