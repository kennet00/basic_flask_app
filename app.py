from flask import Flask

app = Flask(__name__)


@app.route('/')
def yo():
    return '<p>added staging pipeline</p>'
