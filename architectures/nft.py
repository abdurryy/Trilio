
class Collection:
    def __init__(self):
        self.collections = []
    
    def create_collection(self, timestamp, public_key, url, icon, name, description, tags, _ad=None):
        self.id = len(self.collections) + 1
        self.name = name
        self.description = description
        self.tags = tags
        self.icon = icon
        self.url = url
        self.owner = public_key
        self.created_at = timestamp
        self.blacklisted = False
        self.collections.append(self)
        for address in _ad.addresses:
            if address["address"]["pbc"] == public_key:
                address["info"]["collections"].append(self.id)
    
    def validate_collection_name(self, name):
        for collection in self.collections:
            if collection.name == name:
                return False
        
        if len(name) > 4 and len(name) < 15: return True
        return False
    
    def validate_collection_owner(self, public_key, collection_id):
        for collection in self.collections:
            if collection.id == collection_id:
                if collection.owner == public_key:
                    return True
        return False

class Asset:
    def __init__(self):
        self.assets = []
    
    def create_asset(self, timestamp, public_key, collection_id, name, description, _ad=None):
        self.id = len(self.assets) + 1
        self.name = name
        self.description = description
        self.collection_id = collection_id
        self.created_at = timestamp
        self.owner = public_key
        self.trading = False
        self.selling = False
        self.assets.append(self)
        for address in _ad.addresses:
            if address["address"]["pbc"] == public_key:
                address["info"]["assets"].append(self.id)


class Trade:
    def __init__(self):
        self.trades = []
    
    def send_trade(self, timestamp, _to, _from, fassets, tassets):
        self.id = len(self.trades) + 1
        self._to = _to
        self._from = _from
        self.fassets = fassets
        self.tassets = tassets
        self.state = 0 # 0 = pending # 1 = accepted # 2 = decline
        self.created_at = timestamp
        self.trades.append(self)


    


