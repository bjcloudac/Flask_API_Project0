>> How to run this app without doing anything? 

# Flask_API_Project0
*  Create python virtual environment in your working directory **Version optional `python3.10 -m venv .venv`
#
*  On Visual Studio Code, `Command+Shift+P`[Mac] or `Ctrl+Shift+P`[Windows] to search and select python interpreter & select the recoemmended one we created now. Close and reopen terminal or open split terminal to confirm new virtual environment has taken effect. It should startwith (.venv) now. Research for other editors! Or confirm your environment by `which python`.
*  Install flask and other templates like jinja2 with `pip install flask`. These gets installed under .venv/lib/python3.10/site-packages
# 
*  Create a file `touch app.py` and poputate it with from `flask import Flask` and  `app = Flask(__name__)`.  make sure the file name and app name is same. Try `flask run` and go to `http://127.0.0.1:5000` and maje sure we are getting error 404 page not found
# Start with our first API End-Point
* app.py is modified with First_API_Endpoint for `GET` method. access it with http://127.0.0.1:5000/stores
if you are using 'Codespace with GitHub', the EndPoint can be something like `https://sturdy-broccoli-q776j4wrjw4gh4vq4-5000.app.github.dev/stores`. Use an API testing tool like 'Insomnia client' or 'Postman'
### Now we can try sending some JSON Data to the API and observe the 'error405' 'Method not allowed in Insomnia'as there is no POST method allowed so far on this EndPoint to handle this query
* Ex: {
	"Name": "Halifax Store",
	"Items": [{"Book": "Harry Porter", "Price": 98.00}]
}
### So we can create a 'POST Endpoint' and try what if we just create the end point and leave it as `pass` 
* Ex. # POST /store data
@app.route('/addstore', methods=['POST'])
def add_store():
   pass.             # internal server error 502 
*
### Now we have created another Endpoint to add a store like
* Ex. `@app.route('/addstore', methods=['POST'])
def add_store():
    request_data = request.get_json()
    new_store = {
        "Name": request_data["Name"],
        "Items": {"Name": request_data["Items"]["Name"], "Price": request_data["Items"]["Price"]}
    }
    stores.append(new_store)
    return new_store, 201`
Test and observe the new store is getting added. and Code `201` is returned as expected 
### Now that we have added to search through the store names and add item, if a store is found in the 'Query String'
* Ex. # POST /stores/<string:name>/item {name:, price:}
`@app.route('/stores/<string:name>/item', methods=['POST'])
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
    return {"Message": "Store not found"}, 404`
### Now create EndPoint to retrieve a specific store and its Items
* Ex.  # GET /stores/<string:name>
`@app.route('/stores/<string:name>', methods=['GET'])
def get_item(name):
    for store in stores:
        if store["Name"] == name:
            return {"Items": store["Items"]}
    return {"Message": "Store not found"}, 404`
### Now create EndPoint to retrieve a price of an item in a specific store 
* Ex. # GET /stores/<string:name>/<string:item>
`@app.route('/stores/<string:name>/<string:item>', methods=['GET'])
def get_item_price(name, item):
    for store in stores:
        if store["Name"] == name:
            for store_item in store["Items"]:
                if store_item["Name"] == item:
                    return store_item
    return {"Message": "Item not found"}, 404`
## Containerization of Application with Docker 
*
*
#
*
#
*


    
                                                                                                            