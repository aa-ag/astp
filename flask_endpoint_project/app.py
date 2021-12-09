############------------ IMPORTS ------------############
from flask import Flask

############------------ GLOBAL VARIABLE(S) ------------############
app = Flask(__name__)

############------------ FUNCTION(S) ------------############
@app.route('/')
def home_page():
    '''
     this is the home page
     of our application
    '''
    return {'message': 'Hello, Wolrd!'}


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()