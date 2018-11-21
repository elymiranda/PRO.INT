from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html',{'questoes': Question.objects.order_by('-pub_date')})

def exibir_questao(request, id_question):
    return render(request,'question.html',{'questao': Question.objects.get(id=id_question)})

def votar(request,id_question,id_choice):
    question = Question.objects.get(id=id_question)
    choice = question.escolhas.get(id=id_choice)
    choice.vote()
    return redirect('index')

def resultado(request,id_question):
    choices = Question.objects.get(id=id_question).escolhas.all()
    votos = 0
    for escolha in choices:
        votos += escolha.voto.count()

    for escolha in choices:
        try:
            escolha.percentual = ((escolha.voto.count() / votos) * 100)
        except ZeroDivisionError:
            escolha.percentual = 0

        escolha.save()


    return render(request,'results.html',{'questao_resultado': Question.objects.get(id=id_question),
                                          'votos': votos})

def manage(request):
    return render(request, 'manage.html', {'questoes_manage': Question.objects.all()})

def manage_question(request,id_question):
    choices = Choice.objects.all()
    choices_nulas = []
    for choice in choices:
        if choice.question is None:
            choices_nulas.append(choice)
    return render(request,'manage_question.html', {'questao_manage': Question.objects.get(id=id_question), 'escolhas_nulas': choices_nulas})

def alterar_status(request, id_question):
    question_alter = Question.objects.get(id=id_question)
    question_alter.alterar_status()
    return redirect('manage')

def excluir_choice(request,id_question,id_choice):
    question = Question.objects.get(id=id_question)
    choice = question.escolhas.get(id=id_choice)
    choice.dell(id_choice)
    return redirect('manage')

def adicionar_choice(request,id_question,id_choice):
    question = Question.objects.get(id=id_question)
    choice = Choice.objects.get(id=id_choice)
    question.adicionar_choice(choice)
    return redirect('manage')

# from pools.models import *
# q = Question.objects.get(id=1)
# c = q.escolhas.all()[0]
# Vote.objects.create(choice=c)
# q.escolhas.all()