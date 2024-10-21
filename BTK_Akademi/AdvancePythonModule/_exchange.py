
import json
import requests
api_key = ""
api_url = f""

exchange_money = input("Enter the money you want to exchange: ") #USD, TRY
take_money =  input("Enter the money you want to take: ") #TRY
amount = input(f"Enter the amount {exchange_money}: ")
result = requests.get(api_url + exchange_money)
result_json = json.loads(result.text)

print(result.json)