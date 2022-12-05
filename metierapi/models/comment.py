from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser, UserManager


class Comment(models.Model):

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)



