from flask import Flask, render_template, url_for
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
def Start():
    return render_template('start.html')

@app.route("/Home")
def Home():
    return render_template('home.html', posts = posts, title='Home')

@app.route("/About")
def About():
    return render_template('about.html', title = 'About')


if __name__ == "__main__":
    app.run(debug=True)
