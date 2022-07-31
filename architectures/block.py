from datetime import datetime
import hashlib, time

class Block:
    def __init__(self, timestamp, transactions, previous_hash="",addresses = "", collections="", assets="", trades=""):
        self.addresses = addresses
        self.collections = collections
        self.assets = assets
        self.trades = trades
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
                elif transaction.input["type"] == "contract-action":
                    # if collection name is valid continue
                    # create collection
                    if transaction.input["action"] == "collection-creation":
                        is_valid_name = self.collections.validate_collection_name(transaction.input["data"]["name"])
                        if is_valid_name:
                            pbc = self.addresses.get_public_key(transaction.input["data"]["signer"])
                            self.collections.create_collection(datetime.now().timestamp(), pbc, transaction.input["data"]["url"], transaction.input["data"]["icon"], transaction.input["data"]["name"], transaction.input["data"]["description"], transaction.input["data"]["tags"], self.addresses)
                    # fix minting
                    elif transaction.input["action"] == "asset-creation":
                        pbc = self.addresses.get_public_key(transaction.input["data"]["signer"])
                        is_collection_owner = self.collections.validate_collection_owner(pbc, transaction.input["data"]["collection_id"])
                        if is_collection_owner:
                            self.assets.create_asset(datetime.now().timestamp(), pbc, transaction.input["data"]["collection_id"], transaction.input["data"]["name"], transaction.input["data"]["description"], self.addresses)

            except Exception as err:
                print(str(err))
        
        self.status = 1
    
    def get_hash(self):
        return hashlib.sha256(str(self.timestamp).encode('utf-8')+str(self.transactions).encode('utf-8')+str(self.previous_hash).encode('utf-8')).hexdigest()