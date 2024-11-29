import requests
import json

API_URL = "http://127.0.0.1:5000/products"

# Add new products
def add_product(name, description, price):
    data = {"name": name, "description": description, "price": price}
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        print(f"Product added: {response.json()}")
    else:
        print(f"Failed to add product: {response.json()}")

# Get all products
def get_products():
    response = requests.get(API_URL)
    if response.status_code == 200:
        print("Products:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"Failed to retrieve products: {response.json()}")

if __name__ == "__main__":
    add_product("Laptop", "A high-performance laptop", 1200.50)
    add_product("Headphones", "Noise-cancelling headphones", 300.75)
    get_products()
