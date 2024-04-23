
from flask import Flask, request
app = Flask(__name__)

# Static store is added Below:

stores = [  
    {
        "Name": "Toronto Store",
        "Items": [  # List of items
            {
                "Name": "Pen",
                "Price": 8.99
            }
        ]  # End of item
    },   # End of store
    {
        "Name": "New York Store",
        "Items": [ # List of items
        ]  # End of item
    }
    
]  # End of stores  


# GET /stores data
@app.route('/stores', methods=['GET'])
def create_store():
    return  {"Known Stores": stores}    # Placeholder

# # POST /store data
# @app.route('/addstore', methods=['POST'])
# def add_store():
#    pass    # We observe error 502 bad gateway, invalid response from the server

#  POST /store data
@app.route('/addstore', methods=['POST'])
def add_store():
    request_data = request.get_json()
    new_store = {
        "Name": request_data["Name"],
        "Items": {"Name": request_data["Items"]["Name"], "Price": request_data["Items"]["Price"]}
    }
    stores.append(new_store)
    return new_store, 201

# POST /stores/<string:name>/item {name:, price:}
@app.route('/stores/<string:name>/item', methods=['POST'])
def add_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["Name"] == name:
            new_item = {
                "Name": request_data["Name"],
                "Price": request_data["Items"]["Price"]
            }
            store["Items"].append(new_item)
            return new_item, 201
    return {"Message": "Store not found"}, 404


""" Retreive Items of a particular store"""
# GET /stores/<string:name>
@app.route('/stores/<string:name>', methods=['GET'])
def get_item(name):
    for store in stores:
        if store["Name"] == name:
            return {"Items": store["Items"]}
    return {"Message": "Store not found"}, 404


""" Retreive Price of a particular item in a store"""
# GET /stores/<string:name>/<string:item>
@app.route('/stores/<string:name>/<string:item>', methods=['GET'])
def get_item_price(name, item):
    for store in stores:
        if store["Name"] == name:
            for store_item in store["Items"]:
                if store_item["Name"] == item:
                    return store_item
    return {"Message": "Item not found"}, 404
