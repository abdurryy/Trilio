from datetime import datetime

class Blockchain:
    def __init__(self, name="", difficulty=2, minimum_transactions=2):
        self.name = name
        self.difficulty = difficulty
        self.minimum_transactions = minimum_transactions
        self.chain = [
        ]
        self.pending_transactions = [

        ]

    def validate_chain(self):
        for i in range(len(self.chain)):
            if self.chain[i].transactions[0] != "genisis block":
                if self.chain[i].get_hash() != self.chain[i].hash:
                    return False
                
                if self.chain[i].previous_hash != self.chain[i-1].hash:
                    return False
        
        return True


