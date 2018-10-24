from django.shortcuts import render
from perfis.models import Perfil
from django.http import HttpResponse

# Create your views here.
def index(request):

	return render(request, 'index.html')

def exibir(request, perfil_id):

	perfil = getPerfil(perfil_id)
	return render(request, 'perfil.html', {'perfil' : perfil})

def getPerfil(perfil_id):

	perfil = Perfil()

	if perfil_id == 1:
		perfil = Perfil("Daniel", "(86) 99977-4227", "danielmessi13@hotmail.com", "IFPI")
	if perfil_id == 2:
		perfil = Perfil("Vinicius", "(86) 98989-8989", "vikvik98@hotmail.com", "IFPI")

	return perfil