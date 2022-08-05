<h1>Trilio - A blockchain written in Python</h1>
<p><img src="https://img.shields.io/badge/license-MIT-green"> <img src="https://img.shields.io/badge/python-v3.4+-green"> <img src="https://img.shields.io/badge/category-blockchain-green">
</p>
<i>Even though I don't know much about blockchain technology or how it works at all, I've decided to create my own blockchain with consensus algorithm Proof-of-Stake (PoS). I've lately been working with Solidity and been learning about smart-contract development, and during I found it quite fun and interesting. That is why this has and is a very fun project to work on, and even though it might not be classed as a blockchain I've learned a lot during research and improved my Python skills a lot!</i>

<i><br>Contributions are highly appreciated.</i>

<h3>Benifits of Trilio</h3>
<ul>
<li>Ultra fast transactions.</li>
<li>Simple to understand and use.</li>
<li>Integrated smart-contract.</li>
</ul>

<h3>Requirements</h3>
<ul>
<li>Trilio requires <a target="__blank" href="https://www.python.org/downloads/">Python v3.4+</a></li>
</ul>


<h1>Get started with Trilio</h1>

<h3>Installation</h3>

In order to make the installation much faster and simpler, I've uploaded this project to PyPi and you can simply install it using the  `pip`  command below.

```
$ pip install trilio==0.1.3
```

You might also need to pip install these libraries, too.
```
$ pip install datetime
$ pip install hashlib
```

<h3>Make your own Blockchain</h3>
```python
from trilio import Trilio

blockchain = Trilio()
```

<h3>Validate your Blockchain</h3>
```python
from trilio import Trilio

blockchain = Trilio()
valid = blockchain.validate_chain() # True = Valid, False = Invalid
```

<h3>Create a Wallet</h3>
```python
from trilio import Trilio

blockchain = Trilio()
wallet = blockchain.wallet.create_wallet() # Will return json with wallet information
```

<h3>Get wallet Keys</h3>
```python
from trilio import Trilio

blockchain = Trilio()
wallet = blockchain.wallet.create_wallet()
address = wallet["address"]
address["pve"] # Private key
address["pbc"] # Public key
```

<h3>Get wallet Attributes</h3>
```python
blockchain.wallet.get_balance(private_key=<private_key>, public_key=<public_key>) # Get a wallet's balance
blockchain.wallet.get_assets(private_key=<private_key>, public_key=<public_key>) # Get a wallet's assets
blockchain.wallet.get_collections(private_key=<private_key>, public_key=<public_key>) # Get a wallet's collections
```


<h3>Trilio's blockchain attributes</h3>
<p>These blockchain attributes are already set, but you can change them to whatever you desire.</p>

`
myBlockchain.trilio.difficulity = 5
` # change the mining complexity

`
myBlockchain.trilio.name = "MyBlochainName"
` # change the name of your blockchain

`
myBlockchain.trilio.minimum_transactions = 1
` # minimum transactions for each block

<h1>Contact me</h1>
Discord: LocalMOD#3782
