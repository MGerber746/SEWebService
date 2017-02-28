from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.ForeignKey(User)
    current_class = models.ForeignKey('classes.Class')
