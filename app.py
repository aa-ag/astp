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


@app.route('/post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        global posts

        posts.append({
            'title': title,
            'content': content
        })

        return redirect(url_for('blog_page'))
    return render_template('new_post.html')

    
############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    app.run()