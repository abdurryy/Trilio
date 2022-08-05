import hashlib, random

# Addresses
class Wallet:
    def __init__(self):
        self.addresses = []
    
    def create_wallet(self):
        pve = random.randint(100000000000,99999999999999)
        pbc = random.randint(100000000000,99999999999999)
        private_key = "pve"+str(hashlib.sha256(str(pve).encode('utf-8')).hexdigest())
        public_key =  "pbc"+str(hashlib.sha256(str(pbc).encode('utf-8')).hexdigest())
        cred_keys = { 
            "address": {
                "pve":private_key, 
                "pbc":public_key 
            }, 
            "info": {
                "balance":float(0),
                "assets" : [],
                "collections" : []
            }
        }
        if self.validate_address(private_key, public_key) == False:
            self.addresses.append(cred_keys)
            return cred_keys
        else:
            return self.create_address()        

    def get_balance(self, private_key=None, public_key=None):
        r = self.require(private_key, public_key)
        if r == False:
            return "Private and Public keys are required"
            
        for address in self.addresses:
            if address["address"]["pbc"] == public_key and address["address"]["pve"] == private_key:
                return float(address["info"]["balance"])
        
    def get_assets(self, private_key=None, public_key=None):
        r = self.require(private_key, public_key)
        if r == False:
            return "Private and Public keys are required"
            
        for address in self.addresses:
            if address["address"]["pbc"] == public_key and address["address"]["pve"] == private_key:
                return address["info"]["assets"]
    
    def get_collections(self, private_key=None, public_key=None):
        r = self.require(private_key, public_key)
        if r == False:
            return "Private and Public keys are required"
            
        for address in self.addresses:
            if address["address"]["pbc"] == public_key and address["address"]["pve"] == private_key:
                return address["info"]["collections"]
    
    def get_public_key(self, private_key=None):
        if private_key == None:
            return "Failed"
        
        for address in self.addresses:
            if address["address"]["pve"] == private_key:
                return address["address"]["pbc"]
        return "Failed"
    
    def credit_wallet(self, public_key = None, amount = None):
        if public_key == None or amount == None:
            return "Failed"
        
        for address in self.addresses:
            if address["address"]["pbc"] == public_key:
                address["info"]["balance"] += amount
                return address["info"]["balance"]
        return "Failed"


    
    def validate_address(self, private_key=None, public_key=None):
        r = self.require(private_key, public_key)
        if r == False:
            return "Private and Public keys are required"
        
        for address in self.addresses:
            if address["address"]["pbc"] == public_key and address["address"]["pve"] == private_key:
                return True
        return False        

    def require(self, private_key=None, public_key=None):
        if private_key == None or public_key == None:
            return False
        return True