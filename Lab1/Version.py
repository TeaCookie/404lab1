import requests

print(requests.__version__)

res = requests.get("https://raw.githubusercontent.com/TeaCookie/404lab1/main/Version.py")

print(res.text)
