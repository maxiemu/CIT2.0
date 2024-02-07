from flask import Flask, render_template

app = Flask(__name__)


products = {
    'lanyard': {'name': 'LANYARD', 'price': 120, 'image': 'lanyard.jpg'},
    'cite_shirt': {'name': 'CITE SHIRT', 'price': 500, 'image': 'BSIT.jpg'},
    'dept_shirt.html': {'name': 'DEPT. SHIRT', 'price': 500, 'image': 'dept_shirt.html.jpg'},
    'middle_product': {'name': '', 'price': 0, 'image': 'BSIT.jpg'},
    'uniform': {'name': 'UNIFORM', 'price': 1500, 'image': 'uniform.jpg'},
    'polo': {'name': 'POLO', 'price': 700, 'image': 'polo.jpg'},
    'pants': {'name': 'PANTS', 'price': 400, 'image': 'pants.jpg'},
}

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product/<product_id>')
def product(product_id):
    product_details = products.get(product_id)
    if product_details:
        return render_template(f'products/{product_id}.html', product=product_details)
    else:
        return render_template('product_not_found.html')

if __name__ == '__main__':
    app.run(debug=True)
