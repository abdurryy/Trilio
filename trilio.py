from numpy import block
from architectures.blockchain import Blockchain
from architectures.block import Block
from architectures.address import Address
from architectures.transaction import Transaction
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
    
    def create_block(self,addresses):
        nonce = self.trilio.difficulty ** 14

        for i in range(nonce):
            pass

        if len(self.trilio.pending_transactions) >= self.trilio.minimum_transactions:
            # block.hash, block.timestamp, block.transactions, block.previous_hash
            transactions = []
            for i in range(self.trilio.minimum_transactions):
                transactions.append(self.trilio.pending_transactions[i])
            block = Block(datetime.now().timestamp(), transactions, self.trilio.chain[len(self.trilio.chain)-1].hash, addresses)
            self.trilio.chain.append(block)
            return block
        else:
            return False

        
    
    def create_transaction(self, timestamp, data):
        self.trilio.pending_transactions.append(
            Transaction(timestamp,data=data)
        )
    
    def get_transaction(self, data):
        for block in self.trilio.chain:
            for transaction in block.transactions:
                if transaction.hash == data:
                    return transaction

blockchain = Trilio()
address = Address()

my_credientials = address.create_address()["address"]
their_credientials = address.create_address()["address"]

blockchain.create_transaction(datetime.now().timestamp(),
    {
        "type" : "token-transfer",
        "data" : {
            "to" : their_credientials["pbc"],
            "from" : my_credientials["pve"],
            "amount": 50
        }
    }
)


block = blockchain.create_block(address)
print(address.get_balance(their_credientials["pve"], their_credientials["pbc"]))
