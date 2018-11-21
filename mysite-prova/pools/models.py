from django.db import models
from datetime import time
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=30)
    closed = models.BooleanField(default=False)
    pub_date = models.DateField()

    def alterar_status(self):
        if self.closed:
            self.closed = False
        else:
            self.closed = True

        self.save()

    def adicionar_choice(self, choice):
        choice.question = self
        choice.save()

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='escolhas', on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=30)
    percentual = models.IntegerField(default=0)

    def dell(self,id_choice):
        self.question = None
        self.voto.all().delete()
        self.save()

    def vote(self):
        Vote.objects.create(choice=self)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(Choice, related_name="voto", on_delete=models.CASCADE)
    vote_date = models.DateTimeField(default=timezone.now)

