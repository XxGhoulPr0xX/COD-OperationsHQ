import requests

whom = "5512762662"
message = "lol"
params = {'phone': whom, 'message': message, 'key': 'textbelt'}
resp = requests.post("https://textbelt.com/text", data=params)
print(resp.json())
