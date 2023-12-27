from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)
TOKEN = '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'


@app.route('/test')
def index():
    return render_template('лагуна.html')


@app.route('/schedule', methods=['GET'])
def get_schedule():
    with open('schedule.json', 'r', encoding='utf-8') as f:
        schedule = json.load(f)
    return schedule[request.args.get('number')]["09.01.2024"]

@app.route('/zxcvb123')
def autoreload():
    os.system(f'git pull https://{TOKEN}@github.com/BorodinaE/disillusion.git')
    return 'reload success'


app.run(debug=True)