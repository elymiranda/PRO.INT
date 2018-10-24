from django.db import models


# Create your models here.
class Perfil(object):

    def __init__(self, nome='',telefone='', email='', nome_empresa=''):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.nome_empresa = nome_empresa

