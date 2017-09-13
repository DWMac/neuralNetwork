from flask import flask
app = Flask(__name__)



#TEST
@app.route("/")
def hello():
    return "Hello World!"
#TEST
@app.route("/perceptron//getWeights")
def hello():
    return "Hello World!"
#TEST
@app.route("/perceptron//getLearnTable")
def hello():
    return "Hello World!"
