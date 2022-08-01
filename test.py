from trilio import Trilio
from datetime import datetime

_bl = Trilio()

test = _bl.Address.create_address()["address"]
test1 = _bl.Address.create_address()["address"]

_bl.create_transaction(
    datetime.now().timestamp(),
    data = {
        "type" : "contract-action",
        "action" : "collection-creation",
        "data" : {
            "signer" : test1["pve"],
            "name" : "abdurry",
            "description" : "hello",
            "url" : "",
            "icon" : "",
            "tags" : ["levitate", "wavy", "splach", "smash"]
        }
    }
)


_bl.create_transaction(
    datetime.now().timestamp(),
    data = {
        "type" : "contract-action",
        "action" : "asset-creation",
        "data" : {
            "signer" : test1["pve"],
            "name" : "imbett",
            "description" : "hello",
            "quantity" : 2,
            "collection_id" : 1
        }
    }
)


_bl.create_transaction(
    datetime.now().timestamp(),
    data = {
        "type" : "contract-action",
        "action" : "collection-creation",
        "data" : {
            "signer" : test["pve"],
            "name" : "imbetterr",
            "description" : "hello",
            "url" : "",
            "icon" : "",
            "tags" : ["levitate", "wavy", "splach", "smash"]
        }
    }
)

_bl.create_transaction(
    datetime.now().timestamp(),
    data = {
        "type" : "contract-action",
        "action" : "asset-creation",
        "data" : {
            "signer" : test["pve"],
            "name" : "imbet",
            "description" : "hello",
            "quantity" : 2,
            "collection_id" : 2
        }
    }
)

_bl.create_transaction(
    datetime.now().timestamp(),
    data = {
        "type" : "token-transfer",
        "data" : {
            "to" : test["pbc"],
            "from" : test1["pve"],
            "amount": 50
        }
    }
)


# before trade
print(_bl.AssetStorage.assets[0].owner)
_bl.create_transaction(
    datetime.now().timestamp(),
    data = {
        "type" : "asset-transfer",
        "data" : {
            "_to" : test["pbc"],
            "_from" : test1["pve"],
            "tassets" : [],
            "fassets" : [1,2]
        }
    }
)

_bl.create_transaction(
    datetime.now().timestamp(),
    data = {
        "type" : "contract-action",
        "action" : "accept-trade",
        "data" : {
            "signer" : test["pve"],
            "id" : 1
        }
    }
)
