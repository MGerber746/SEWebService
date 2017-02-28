from django.contrib.auth.models import User
from django.db import models


class Teacher(models.Model):
    user = models.ForeignKey(User)
    school_name = models.CharField(max_length=100)
