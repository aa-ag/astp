############------------ IMPORTS ------------############
from flask import Flask, render_template, request, redirect, url_for


############------------ GLOBAL ------------################
app = Flask(__name__)

posts = []

############------------ ROUTE(S) ------------############
@app.route('/')
def homepage():
    return render_template('home.html')
    

############------------ DRIVER CODE ------------############
if __name__ == '__main__':
    app.run()