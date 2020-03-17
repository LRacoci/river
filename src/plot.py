with open(".keys/binance/api") as f:
    api_key = f.read()

with open(".keys/binance/secret") as f:
    api_secret = f.read()

from binance.client import Client
client = Client(api_key, api_secret)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

import json 
print(json.dumps(depth, indent=4))