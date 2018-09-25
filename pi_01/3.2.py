import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.google.com")
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

for link in soup.find_all('a'):
    print(link['href'])
