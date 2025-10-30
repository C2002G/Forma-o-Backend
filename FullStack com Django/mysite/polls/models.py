from datetime import datetime 
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=True)  # ativo ou n ativo
    x = models.TextField()

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Opção"
        verbose_name_plural = "Opções"

    def __str__(self):
        return f'{self.question.id}: {self.choice_text}'

