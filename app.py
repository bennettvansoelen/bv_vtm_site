from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/price', methods=['GET'])
def price():
    return render_template('price.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        pi = 3.14
        r = float(request.form['radius'])
        h = float(request.form['height'])
        topArea = pi * (r ** 2)
        sideArea = 2 * (pi * (r * h))
        totalArea = topArea + sideArea
        sqftArea = totalArea/144
        materialCost = 25 * sqftArea
        laborCost = 15 * sqftArea
        totalCost = materialCost + laborCost
        print(totalCost)
    return render_template('price.html', myValue= totalCost)


if __name__ == '__main__':
    app.run(debug=True)