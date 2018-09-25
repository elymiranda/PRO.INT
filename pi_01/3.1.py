from bs4 import BeautifulSoup
import requests

page = 1
links = set()
length = 0

while True:
    print("Page {}".format(page))
    gofundme = requests.get('http://www.google.com'.format(page))
    soup = BeautifulSoup(gofundme.content, "html.parser")
    links.update([a['href'] for a in soup.find_all('a', href=True)])

    # Stop when no new links are found
    #if len(links) == length:
    #    break

    if page == 1:
        break

    length = len(links)
    page += 1

for link in sorted(links):
    print(link)