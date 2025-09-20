import requests
import json

url = "https://api-example-falguni.onrender.com/add"

querystring = {"x":"5","y":"7"}



response = requests.get(url, params=querystring)

print(json.dumps(response.json(),indent=4))
