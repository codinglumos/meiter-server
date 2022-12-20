from django.db import models
from django.contrib.auth.models import User


class Reaction(models.Model):

    reaction = models.CharField(max_length=50)
