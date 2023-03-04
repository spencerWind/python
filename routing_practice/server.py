from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<string:name>')
def say_name(name):
    return "Hello " + name 

@app.route('/repeat/<int:num>/<string:phrase>')
def repeat(num, phrase):
    return f"{phrase * num}"

@app.errorhandler(404)
def not_found(e):
    return "Sorry! No response! Try again!"

if __name__ == "__main__":
    app.run(debug = True, port = 5001)
    
