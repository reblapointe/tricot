from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/broches')
def broches():
    return render_template('broches.html')


@app.route('/echantillon')
def echantillon():
    return render_template('echantillon.html')
