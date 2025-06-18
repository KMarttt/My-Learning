import json
import requests
import sys

try:
    n = float(input("Number of BitCoins: "))
except ValueError:
    sys.exit("User-input is not a number")

bitcoins_data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
"""A way to look at the whole json datas"""
# print(json.dumps(bitcoins_data.json(), indent=2))
# Remember: json.dumps with s at the end

bit_coin_json = bitcoins_data.json()
rate_value = (bit_coin_json ["bpi"]["USD"]["rate"])
# so you can just do this to access data inside a dictionary that is inside another dict
# bit_coin_json is the name of the orig dict and the ["names"] is the series of key names to get to the value of key that' i'm looking for
rate_value = rate_value.replace(",","")
amount = float(rate_value) * n
print(f"${amount:,.4f}")


