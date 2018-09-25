import requests

url = 'http://www.google.com'
response = requests.get(url)
print(response.status_code)
print(response.headers)
print(len(response.content))