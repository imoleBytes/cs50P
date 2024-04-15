#!/usr/bin/python3
import requests
import sys


if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")

try:
    num = float(sys.argv[1])
except Exception:
    sys.exit("Command-line argument is not a number")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    result = requests.get(url).json()
    price = result['bpi']['USD']['rate_float']
    total = price * num
    print(f"${total:,.4f}")
except requests.RequestException as e:
    print(e)
