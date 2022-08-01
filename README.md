<h1>Trilio - A blockchain written in Python</h1>
<p><img src="https://img.shields.io/badge/license-MIT-green"> <img src="https://img.shields.io/badge/python-v3.4+-green"> <img src="https://img.shields.io/badge/category-blockchain-green">
</p>
<i>Even though I don't know much about blockchain technology or how it works at all, I've decided to create my own blockchain with consensus algorithm Proof-of-Stake (PoS). I've lately been working with Solidity and been learning about smart-contract development, and during I found it quite fun and interesting. That is why this has and is a very fun project to work on, and even though it might not be classed as a blockchain I've learned a lot during research and improved my Python skills a lot!</i>

<i><br>- Contributions are highly appreciated.</i>

<h3>Benifits of Trilio</h3>
<ul>
<li>Ultra fast transactions.</li>
<li>Simple to understand.</li>
<li>Easy to use.</li>
</ul>

<h3>Requirements</h3>
<ul>
<li>Trilio requires <a href="https://www.python.org/downloads/">Python v3.4+</a></li>
</ul>


<h1>Get started with Trilio</h1>

<h3>Installation</h3>

In order to make the installation much faster and simpler, I've uploaded this project to PyPi and you can simply install it using the  `pip`  command below.

```
$ pip install trilio==0.1.2
```

You might also need to pip install these libraries, too.
```
$ pip install datetime
$ pip install hashlib
```

<h3>Create your first valid blockchain</h3>

Here is a simple way to create your own blockchain with Trilio and check if the chain is valid, with that we mean whether or not the chain has been compromised. This will return a boolean value such as `True` or `False`, where `True` corresponds to validity.

<p></p>

```python
from trilio import Trilio

# make your own blockchain
myBlockchain = Trilio()

# check if chain is valid
IsChainValid = myBlockchain.validate_chain()

print("Is my chain valid", IsChainValid)
```

<h3>Create your first wallet</h3>

```python
from trilio import Trilio

# make your own blockchain
myBlockchain = Trilio()

# create your own wallet
myWallet = myBlockchain.Address.create_address()

# wallet
myWalletAddress = myWallet["address"]

# wallet keys
myPrivateKey = myWalletAddress["pve"] # pve = private
myPublicKey = myWalletAddress["pbc"] # pbc = public

print(myPublicKey, myPrivateKey)
```

<h3>Contact me</h3>
Discord: LocalMOD#3782
