from architectures.blockchain import Blockchain
from architectures.block import Block
from architectures.address import Address
from architectures.transaction import Transaction
from architectures.nft import Collection, Trade, AssetStorage
from datetime import datetime

class Trilio:
    def __init__(self):
        self.trilio = Blockchain(
            name="Trilio", 
            difficulty=4,
            minimum_transactions=1
        )
        # Create genisis
        self.trilio.chain.append(Block(datetime.now().timestamp(), ["genisis block"]))
    
    def create_block(self,addresses=None, collections=None, assets=None, trades=None):
        nonce = self.trilio.difficulty ** 12

        for i in range(nonce):
            pass

        if len(self.trilio.pending_transactions) >= self.trilio.minimum_transactions:
            # block.hash, block.timestamp, block.transactions, block.previous_hash
            transactions = self.trilio.pending_transactions
            self.trilio.pending_transactions = []
            
            block = Block(datetime.now().timestamp(), transactions, self.trilio.chain[len(self.trilio.chain)-1].hash, addresses, collections, assets, trades)
            self.trilio.chain.append(block)
            return block
        else:
            return False
        

        
    
    def create_transaction(self, timestamp, data):
        self.trilio.pending_transactions.append(
            Transaction(timestamp,data=data)
        )
        self.create_block(
            addresses=_ad,
            collections=_co,
            trades=_tr,
            assets=_as
        )
    

    def get_transaction(self, data):
        for block in self.trilio.chain:
            for transaction in block.transactions:
                if transaction.hash == data:
                    return transaction

_bl = Trilio()
_ad = Address()
_tr = Trade()
_co = Collection()
_as = AssetStorage()


test = _ad.create_address()["address"]
test1 = _ad.create_address()["address"]

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

print(_ad.get_assets(test["pve"],test["pbc"]))
print(_ad.get_assets(test1["pve"],test1["pbc"]))

# before trade
print(_as.assets[0].owner)
_bl.create_transaction(
    datetime.now().timestamp(),
    data = {
        "type" : "asset-transfer",
        "data" : {
            "_to" : test["pbc"],
            "_from" : test1["pve"],
            "tassets" : [],
            "fassets" : [1]
        }
    }
)


# under trade
print(_as.assets[0].owner)


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

#after trade
print(_as.assets[0].owner)

print(_ad.get_assets(test["pve"],test["pbc"]))
print(_ad.get_assets(test1["pve"],test1["pbc"]))

# trade.send_trade(datetime.now().timestamp(), test["pbc"], test1["pve"], [10], [])

