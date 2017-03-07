from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=100)
    math_type = models.CharField(max_length=100)
