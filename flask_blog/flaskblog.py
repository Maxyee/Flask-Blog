from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/Home")
def Home():
    return "This is Home page"

@app.route("/About")
def About():
    return "This is About page"


if __name__ == "__main__":
    app.run(debug=True)