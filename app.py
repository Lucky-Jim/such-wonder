from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "O brave new world, that hath such people in it!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
