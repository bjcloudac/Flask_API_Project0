
from flask import Flask
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
    }   # End of store
    
]  # End of stores  


# POST /store data: {name:}
@app.route('/stores', methods=['GET'])
def create_store():
    return  {"Known Stores": stores}    # Placeholder