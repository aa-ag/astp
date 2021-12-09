############------------ IMPORTS ------------############
from flask import Flask, jsonify

############------------ GLOBAL VARIABLE(S) ------------############
app = Flask(__name__)

############------------ FUNCTION(S) ------------############
@app.route('/')
def home_page():
    '''
     this is the home page
     of our application
    '''
    return jsonify({'message': 'Hello, Wolrd!'})


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()