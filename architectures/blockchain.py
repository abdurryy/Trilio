#blockchain
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


