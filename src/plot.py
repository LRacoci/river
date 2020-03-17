with open(".keys/binance/api") as f:
    api_key = f.read()

with open(".keys/binance/secret") as f:
    api_secret = f.read()

from binance.client import Client
client = Client(api_key, api_secret)
depth = client.get_order_book(symbol='BTCUSDT')

depths = {key: [] for key in depth}

import json


for _ in range(10):
    depth = client.get_order_book(symbol='BTCUSDT')
    for key in depth:
        if key in depths:
            depths[key].append(depth[key])
            print(json.dumps(depth, indent=4))

from datetime import datetime
time = int(datetime.now().timestamp())

with open(f"depths-{time}.json", "a") as f:
    json.dump(depths, f)

print(json.dumps(depths, indent=4))