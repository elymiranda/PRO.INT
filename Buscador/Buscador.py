import requests
from bs4 import BeautifulSoup
import re


# Comparador de preços

def main():

    palavra = input("Palavra : ")
    profundidade = int(input("Profundidade da pesquisa: "))

    url = 'http://www.ifpi.edu.br/'
    get_links(url, profundidade, palavra)


def get_links(url, profundidade, palavra):
    if profundidade == 0:
        return get_palavra(url,palavra)

    links = []

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    a = soup.find_all("a")

    for link in a:
        try:
            if (str(link['href']).startswith("http")):
                links.append(link["href"])
                print(link["href"])
                print("Profundidade " + str(profundidade))
                get_palavra(link["href"], palavra)
        except:
            pass

    profundidade -= 1

    if profundidade > 0:
        get_super_links(links, profundidade, palavra)

    return links


def get_super_links(urls, profundidade, palavra):

    links = []

    for i in urls:
        links.append(get_links(i, profundidade, palavra))

    return links


def get_palavra(link, palavra):
    response = requests.get(link)

    text = clear(BeautifulSoup(response.text, "html.parser")).text

    encontradas = re.findall('\w*.{0,10}' + palavra + '.{0,10}\w*', text, re.IGNORECASE)

    for encontrada in encontradas:
        print(encontrada)


def clear(text):
    body = text.body

    for script in body(["script", "style"]):
        script.decompose()

    return body


if __name__ == '__main__':
    main()
