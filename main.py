from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route('/test')
def index():
    return render_template('лагуна.html')


@app.route('/schedule', methods=['GET'])
def get_schedule():
    with open('schedule.json', 'r', encoding='utf-8') as f:
        schedule = json.load(f)
    return schedule[request.args.get('number')]["09.01.2024"]


app.run(debug=True)