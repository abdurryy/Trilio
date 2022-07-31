# Haven't been focusin on this one


from flask import Flask, jsonify, request
from datetime import datetime

from trilio import Trilio
from architectures.blockchain import Blockchain
from architectures.block import Block
from architectures.address import Address
from architectures.transaction import Transaction

app = Flask(__name__)
blockchain = Trilio()
address = Address()

# Example create_address request: requests.post("http://127.0.0.1:5000/api/create_address")
@app.route("/api/create_address", methods=["POST"])
def create_address():
    try:
        credientials = address.create_address()["address"]
        response = {
            "status":"success",
            "pve":credientials["pve"],
            "pbc":credientials["pbc"],
        }
        return jsonify(response)
    except Exception as err:
        response = {
            "status":"failure",
            "err":str(err)
        }
        return jsonify(response)

# Example create_transaction request: requests.post("http://127.0.0.1:5000/api/create_transaction", json={ "type":"transfer", "data": { "to": <to>, "from": <private_key>, "amount": <amount> } })
@app.route("/api/", methods=["POST"])
def create_transaction():
    try:
        request.get_json(force=True)
        blockchain.create_transaction(
            datetime.now().timestamp(),
            request.get_json(force=True)
        )
        response = {
            "status":"success",
            "msg":"transaction is now pending."
        }
        return jsonify(response)
    except Exception as err:
        response = {
            "status":"failure",
            "err":str(err)
        }
        return jsonify(response)



app.run("localhost", port=5000, debug=True)
