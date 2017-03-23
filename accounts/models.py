from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.ForeignKey(User)

    def __str__(self):
        return self.user.get_full_name()


class Teacher(models.Model):
    user = models.ForeignKey(User)
    school_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()
