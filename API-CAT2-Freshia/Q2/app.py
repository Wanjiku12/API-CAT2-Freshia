from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

# POST /products - Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({'error': 'Invalid input data'}), 400
    try:
        new_product = {
            'id': len(products) + 1,
            'name': data['name'],
            'description': data['description'],
            'price': float(data['price'])
        }
        products.append(new_product)
        return jsonify(new_product), 201
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid price format'}), 400

# GET /products - Retrieve all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
