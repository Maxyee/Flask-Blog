from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author':'Eyamin Khan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 18 , 2017'
    },
    {
        'author':'neshat Mahee',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 20 , 2017'
    }
]

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/Home")
def Home():
    return render_template('home.html', posts = posts)

@app.route("/About")
def About():
    return "This is About page"


if __name__ == "__main__":
    app.run(debug=True)
