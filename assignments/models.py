from django.db import models


class Assignment(models.Model):
    teacher = models.ForeignKey('accounts.Teacher')
    questions = models.ManyToManyField('assignments.Question', blank=True)
    name = models.CharField(max_length=100)


class Question(models.Model):
    game_type = models.ForeignKey('games.Game')
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
