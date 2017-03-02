from django.contrib.auth.models import User
from django.db import models


class Grade(models.Model):
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    student = models.ForeignKey('accounts.Student')
