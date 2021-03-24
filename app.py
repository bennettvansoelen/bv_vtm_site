from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mike')
def mike():
    return render_template('mike.html')

@app.route('/price', methods=['GET'])
def price():
    return render_template('price.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        pi = 3.14
        r = float(request.form['radius'])
        h = float(request.form['height'])
        topArea = pi * (r**2)
        print(topArea)
    return render_template('price.html', myValue= topArea)

if __name__ == '__main__':
    app.run(debug=True)