from flask import Flask, render_template

app = Flask(__name__)

@app.route('/test')
def index():
    return render_template('лагуна.html')


app.run(debug=True)

