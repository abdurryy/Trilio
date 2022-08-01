# Transactions
import hashlib

class Transaction:
    def __init__(self, timestamp, data):
        self.timestamp = timestamp
        self.input = data
        self.hash = self.get_hash()
    
    def get_hash(self):
        return hashlib.sha256(str(self.timestamp).encode('utf-8')+str(self.input).encode('utf-8')).hexdigest()
    