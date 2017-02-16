from django.contrib.auth.models import User
from django.db import models


from accounts.constants import USER_ACCOUNT_TYPE_CHOICES


class UserAccount(User):
    type = models.CharField(max_length=10, choices=USER_ACCOUNT_TYPE_CHOICES)
