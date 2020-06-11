from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "版本v.1功能"


if __name__ == '__main__':
    app.run(debug=True)
