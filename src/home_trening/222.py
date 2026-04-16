from typing import Dict

import requests

# import requests
#
# url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=10"
#
# payload = {}
# headers= {
#   "apikey": "s2zlwBrMNJrGPwTWh8KnARzLpZOVbtV6"
# }
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text
#
# {
#   "date": "2026-04-04",
#   "info": {
#     "rate": 92.536885,
#     "timestamp": 1775323747
#   },
#   "query": {
#     "amount": 10,
#     "from": "EUR",
#     "to": "RUB"
#   },
#   "result": 925.36885,
#   "success": true
# }

def get_convert(transaction: Dict) -> float:
    currency_code = transaction.get("operationAmount").get("currency").get("code")
    amount = transaction.get("operationAmount").get("amount")
    if currency_code == "RUB":
        return float(amount)

    elif currency_code in ["USD", "EUR"]:
        data = {"from": currency_code, "to": "RUB", "amount": amount}
        url = "https://api.apilayer.com/exchangerates_data/convert"
        headers = {"apikey": "cOGzKNwrGlM7ctnn8S0xnv8Gzy9x7epe"}

    response = requests.get(url, headers=headers, params=data)
    print(response.json())
    return float(response.json().get("result"))
