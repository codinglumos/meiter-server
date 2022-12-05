from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser, UserManager


class Reaction(models.Model):

    reaction = models.CharField(max_length=50)