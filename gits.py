from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "约饭功能版本"


if __name__ == '__main__':
    app.run(debug=True)
