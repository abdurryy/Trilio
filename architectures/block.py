import hashlib

class Block:
    def __init__(self, timestamp, transactions, previous_hash="",addresses = ""):
        self.addresses = addresses
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.get_hash()
        self.status = 0 # 0 = pending, 1 = completed 
        self.complete()
    
    def complete(self):

        for transaction in self.transactions:
            try:
                try:
                    pbc = self.addresses.get_public_key(transaction.input["data"]["from"])
                    pve = transaction.input["data"]["from"]
                except:
                    pass

                if transaction == "genisis block":
                    return
                if transaction.input["type"] == "token-transfer":
                    if float(transaction.input["data"]["amount"]) >= 0:
                        if self.addresses.get_balance(pve, pbc) >= float(transaction.input["data"]["amount"]):
                            self.addresses.credit_address(transaction.input["data"]["to"], float(transaction.input["data"]["amount"]))
                            self.addresses.credit_address(pbc, -float(transaction.input["data"]["amount"]))
            except Exception as err:
                print(str(err))
        
        self.status = 1
    
    def get_hash(self):
        return hashlib.sha256(str(self.timestamp).encode('utf-8')+str(self.transactions).encode('utf-8')+str(self.previous_hash).encode('utf-8')).hexdigest()