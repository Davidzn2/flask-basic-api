from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': "Store",
        'items':[
            {
                'name':'Item',
                'price': 12
            }
        ]
    },
]

@app.route('/')
def home():
    return "Hello, world"

@app.route('/store/', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>/', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'Not found'})

@app.route('/store/')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item/', methods=['POST'])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'Not found'})


@app.route('/store/<string:name>/item/', methods=['GET'])
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'Not found'})

app.run(port=8080)