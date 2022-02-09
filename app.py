############------------ IMPORTS ------------############
from flask import Flask, render_template, request, redirect, url_for


############------------ GLOBAL ------------################
app = Flask(__name__)

posts = []


############------------ ROUTE(S) ------------############
@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/blog')
def blog_page():
    return render_template('blog.html', posts=posts)

############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    app.run()