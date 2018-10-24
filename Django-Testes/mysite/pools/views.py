from django.shortcuts import render
from pools.models import Question

# Create your views here.

def index(request):
    return render(request, 'index.html')

def question(request, id):
    question = get_question(id)
    return render(request, 'question.html', {'question' : question})

def get_question(id):
    question = Question()

    if id == 1:
        question = Question("Qual sua idade?", "10/10/1999")
    if id == 2:
        question = Question("Qual seu nome?", "11/02/2010")
    if id == 3:
        question = Question("Qual sua cor?", "23/12/2018")

    return question