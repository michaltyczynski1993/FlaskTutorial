from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"
@app.route("/about")
def about(xyz):
    return "It is about Page"


if __name__ == "__main__":
    app.run(debug=True, port=5001)