# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re




def main():
    # Comparador de preços
    url = input("Link: ")
    palavra = input("Palavra : ")
    profundidade = int(input("Profundidade da pesquisa: "))

    get_links(url, profundidade, palavra)


def get_links(url, profundidade, palavra):


    links = []

    if profundidade == 0:
        return get_palavra(url,palavra)

    response = requests.get(url)

    if response is not None:
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")
            a = soup.find_all("a")

            for link in a:
                try:
                    if (str(link['href']).startswith("http")):
                        if link["href"] not in links:
                            links.append(link["href"])
                            print(link["href"])
                            print("Profundidade " + str(profundidade))
                            get_palavra(link["href"], palavra)
                except:
                    pass


            if profundidade > 0:
                get_super_links(links, profundidade-1, palavra)

            return links


def get_super_links(urls, profundidade, palavra):

    links = []

    for i in urls:
        links.append(get_links(i, profundidade, palavra))

    return links


def get_palavra(link, palavra):

    response = requests.get(link)

    text = clear(BeautifulSoup(response.text, "html.parser")).text

    encontradas = re.findall('\w*.{0,11}' + palavra + '.{0,11}\w*', text, re.IGNORECASE)

    for encontrada in encontradas:
        print(encontrada)


def clear(text):

    body = text.body

    for script in body(["script", "style"]):
        script.decompose()

    return body


if __name__ == '__main__':
    main()
