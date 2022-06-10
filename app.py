import requests
import base64
import config

url = "https://api.channeladvisor.com/oauth2/token"

auth_str = '{}:{}'.format(config.app_id, config.client_secret)
b64_auth_str = base64.urlsafe_b64encode(auth_str.encode()).decode()

payload = 'grant_type=refresh_token&refresh_token=' + config.refresh_token
headers = {
    'Authorization': 'Basic ' + b64_auth_str,
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print("JSON Response ", response.json())
