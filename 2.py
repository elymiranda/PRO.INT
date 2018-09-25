import os
import requests

imagem = open("imagem.jpg", "wb")
r = requests.get('http://craphound.com/images/1006884_2adf8fc7.jpg')

imagem.write(r.content)
imagem.close()