from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
    return jsonify({"message":"PONG!"})

@app.route('/products', methods=['GET']) # el parametro methods viene por mdefecto GET si no se coloca
def getProducts():
    return jsonify({"products" : products, "message":"Products list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    print (product_name)

    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound) > 0):
        return jsonify({"product":productFound[0]})
    return jsonify({"message":"Product not Found"})

@app.route('/products', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }

    products.append(new_product)

    return jsonify({"message":"Product added succesfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if( len(productFound) > 0 ):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']

        return jsonify({
            "message" : "product updated",
            "product" : productFound
        })
    return jsonify({"message":"Product not Found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if( len(productFound) > 0 ):
        products.remove(productFound[0])
        return jsonify({
            "message" : "Product deleted",
            "products" : products
        })
    return jsonify({"message":"Product not Found"})

if __name__ == "__main__":
    app.run(debug='true', port=4000)