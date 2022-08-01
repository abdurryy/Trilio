
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

class AssetStorage:
    def __init__(self):
        self.assets = []


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
    
    def accept_trade(self, id, private_key, address, assets, _ad):
        
        for trade in self.trades:
            if trade.id == id:
                if trade.state == 2 or trade.state == 1:
                    return # This trade has already been interacted with
                if trade._to == address.get_public_key(private_key):
                    tassets = 0
                    for asset_id in trade.tassets:
                        for asset in assets.assets:
                            if asset.id == asset_id and asset.owner == trade._to:
                                tassets += 1
                    if tassets == len(trade.tassets):
                        for asset_id in trade.tassets:
                            assets.assets[asset_id-1].owner = address.get_public_key(trade._from)
                            for address in address.addresses:
                                if address["address"]["pve"] == trade._from:
                                    address["info"]["assets"].append(asset_id)
                            for address in _ad.addresses:
                                if address["address"]["pbc"] == trade._to:
                                    address["info"]["assets"].pop(address["info"]["assets"].index(asset_id))

                                    

                        for asset_id in trade.fassets:
                            assets.assets[asset_id-1].owner = trade._to
                            for address in _ad.addresses:
                                if address["address"]["pbc"] == trade._to:
                                    address["info"]["assets"].append(asset_id)
                                
                                

                        trade.state = 1
                else:
                    print("worng address")


    


