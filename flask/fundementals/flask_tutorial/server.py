from flask import Flask, render_template

app = Flask(__name__)

name = 'fred'
row = {
    'id': 3,
    'first_name': 'John',
    'last_name': 'Winvhester'

}
items = ['apple', 'flask', 'rum']


@app.route('/')
def display_home( name=name, row=row, items=items):
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, port=5001)