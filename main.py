from flask import Flask, render_template, request
import json
import reload
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

pass

@app.route('/git_update')
def autoreload():
    os.system(f'git pull https://{TOKEN}@github.com/BorodinaE/disillusion.git')
    with open('reload.py', 'w+') as f:
        f.write('pass;')
    return 'reload success'


app.run(debug=True)
