<h1>Trilio - A blockchain written in Python</h1>
<p><img src="https://img.shields.io/badge/license-MIT-green"> <img src="https://img.shields.io/badge/python-v3.4+-green"> <img src="https://img.shields.io/badge/category-blockchain-green">
</p>
<i>Even though I don't know much about blockchain technology or how it works at all, I've decided to create my own blockchain with consensus algorithm Proof-of-Stake (PoS). I've lately been working with Solidity and been learning about smart-contract development, and during I found it quite fun and interesting. That is why this has and is a very fun project to work on, and even though it might not be classed as a blockchain I've learned a lot during research and improved my Python skills a lot!</i>

<h3>UPDATE: I see a lot of things I could improve when I revisit this project.</h3>

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

<h1>Usage</h1>

- [Getting Started with Trilio](#getting-started-with-Trilio)
  - [Requirements](#requirements)
  - [Installation](#installation)
- [Usage Examples](#usage-examples)
  - [Blockhain](#blockchain)
    - [Make your own Blockchain](#make-your-own-blockchain)
    - [Validate your Blockchain](#validate-your-Blockchain)
    - [Trilio's blockchain attributes](#Trilios-blockchain-attributes)
  - [Wallet](#wallet)
    - [Create a Wallet](#create-a-wallet)
    - [Get wallet Keys](#get-wallet-keys)
    - [Convert wallet Key](#convert-wallet-key)
    - [Credit a Wallet](#credit-a-wallet)
    - [Validate a Wallet](#validate-a-wallet)
  - [Transactions](#transactions)
    - [Send tokens to Wallet](#send-tokens-to-wallet)
    - [Send trade to Wallet](#send-trade-to-wallet-currently-broken)
    - [Accept a Trade](#accept-a-tradecurrently-broken)
    - [Decline a Trade](#decline-a-tradecurrently-broken)
    - [Create your Collection](#create-your-collection)
    - [Create your Asset](#create-your-asset)
- [Contact Me](#contact-me)
- [License](#license)


<h1>Get started with Trilio</h1>

<h3>Installation</h3>

In order to make the installation much faster and simpler, I've uploaded this project to PyPi and you can simply install it using the  `pip`  command below.

```
$ pip install trilio==0.1.9
```

You might also need to pip install these libraries, too.
```
$ pip install datetime
$ pip install hashlib
```
<h1>Usage Examples</h1>
<p>I guarantee you that if you try to understand you will understand. The code examples should <br>explain themselves.</p>
<h2>Blockchain</h2>
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

<h3>Trilio's blockchain attributes</h3>
<p>These blockchain attributes are already set, but you can change them to whatever you desire.</p>

`
blockchain.trilio.difficulity = 5
` # change the mining complexity

`
blockchain.trilio.name = "MyBlochainName"
` # change the name of your blockchain

`
blockchain.trilio.minimum_transactions = 1
` # minimum transactions for each block

<h2>Wallet</h2>
<h3>Create a Wallet</h3>

```python
from trilio import Trilio

blockchain = Trilio()
wallet = blockchain.Wallet.create_wallet() # Will return json with wallet information
```

<h3>Get wallet Keys</h3>

```python
from trilio import Trilio

blockchain = Trilio()
wallet = blockchain.Wallet.create_wallet()
address = wallet["address"]
address["pve"] # Private key
address["pbc"] # Public key
```

<h3>Get wallet Attributes</h3>

```python
blockchain.Wallet.get_balance(private_key=<private_key>, public_key=<public_key>) # Get a wallet's balance
blockchain.Wallet.get_assets(private_key=<private_key>, public_key=<public_key>) # Get a wallet's assets
blockchain.Wallet.get_collections(private_key=<private_key>, public_key=<public_key>) # Get a wallet's collections
```

<h3>Convert wallet Key</h3>

```python
blockchain.Wallet.get_public_key(private_key=<private_key>)
```

<h3>Credit a Wallet</h3>

```python
blockchain.Wallet.credit_wallet(public_key=<public_key>, amount=<amount>)
```

<h3>Validate a Wallet</h3>

```python
blockchain.Wallet.validate_wallet(private_key=<private_key>, public_key=<public_key>) # True = found, False = not found
```

<h2>Transactions</h2>
<h3>Send tokens to Wallet</h3>

```python
# Need to import datetime
blockchain.create_transaction(
    datetime.now(),
    data = {
        "type":"token-transfer",
        "data":{
            "to":<public_key (Wallet recieving)>,
            "from":<private_key (Wallet sending)>,
            "amount":<amount>
        }
    }
)
```

<h3>Send trade to Wallet (currently broken)</h3>

```python
# Need to import datetime
blockchain.create_transaction(
    datetime.now(),
    data={
        "type":"asset-transfer",
        "data":{
            "_to":<public_key_receiver>,
            "_from":<private_key_sender>,
            "fassets":[<sending_assets_id>],
            "tassets":[<receiving_assets_id>]
        }
    }
)
```

<h3>Accept a Trade(currently broken)</h3>

```python
# Need to import datetime
blockchain.create_transaction(
    datetime.now(),
    data={
        "type":"contract-action",
        "action":"accept-trade",
        "data":{
            "id":<trade_id>,
            "signer":<private_key>
        }
    }
)
```

<h3>Decline a Trade(currently broken)</h3>

```python
# Need to import datetime
blockchain.create_transaction(
    datetime.now(),
    data={
        "type":"contract-action",
        "action":"decline-trade",
        "data":{
            "id":<trade_id>,
            "signer":<private_key>
        }
    }
)
```

<h3>Create your Collection</h3>
<p>Collections are used to sort assets/NFTs to different categories, therefore we can also call collections "categories".</p>

```python
# Need to import datetime
blockchain.create_transaction(
    datetime.now(),
    data = {
        "type":"contract-action",
        "action":"collection-creation",
        "data":{
            "name":<collection_name>,
            "description":<collection_description>,
            "url":<collection_url>,
            "icon":<collection_icon>,
            "tags":<collection_tags>,
            "signer":<private_key>
        }
    }
)

#print(blockchain.Wallet.get_collections(private_key=<private_key>, public_key=<public_key>))
```

<h3>Create your Asset</h3>
<p>Assets are basically a fancy name for NFTs, you would need a collection owned by you to mint an NFT.</p>

```python
# Need to import datetime
blockchain.create_transaction(
    datetime.now(),
    data={
        "type":"contract-action",
        "action":"asset-creation",
        "data":{
            "name":<asset_name>,
            "description":<asset_description>,
            "collection_id":<collection_id>,
            "quantity":<asset_mint_amount>,
            "signer":<private_key>
        }
    }
)

#print(blockchain.Wallet.get_assets(private_key=<private_key>, public_key=<public_key>))
```

<h1>Contact me</h1>
Discord: LocalMOD#3782

<h1>License</h1>
<p>Check out Trilio's <a href="https://github.com/abdurryy/Trilio/blob/master/LICENSE.txt">license</a>.</p>
