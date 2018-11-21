"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pools import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:id_question>', views.exibir_questao, name='question'),
    path('question/<int:id_question>/votar/<int:id_choice>', views.votar, name='votar'),
    path('question/<int:id_question>/results', views.resultado, name='resultado'),
    path('manage', views.manage, name='manage'),
    path('question/<int:id_question>/manage', views.manage_question, name='manage_question'),
    path('question/<int:id_question>/manage/alterar_status', views.alterar_status, name='alterar_status'),
    path('question/<int:id_question>/manage/excluir_choice/<int:id_choice>', views.excluir_choice, name='excluir_choice'),
    path('question/<int:id_question>/manage/adicionar_choice/<int:id_choice>', views.adicionar_choice, name='adicionar_choice'),
]
