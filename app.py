from flask import Flask

app = Flask(__name__)


@app.route('/')
def yo():
    return '<p>yo yo new version</p>'
