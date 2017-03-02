from django.contrib.auth.models import User
from django.db import models


class Class(models.Model):
    teacher = models.ForeignKey('accounts.Teacher')
    students = models.ManyToManyField('accounts.Student')
    name = models.CharField(max_length=100)
