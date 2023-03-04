from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/play')
def play():
    return render_template('play.html')

@app.route('/play/<int:x>')
def play_num(x):
    return render_template('playnum.html',x=x)

@app.route('/play/<int:x>/<string:color>')
def play_num_color(x, color):
    return render_template('playnumcolor.html',x=x, color=color)
    
if __name__ == "__main__":
    app.run(debug=True, port=5001)