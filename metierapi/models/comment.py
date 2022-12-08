from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_on = models.DateTimeField(null=True, blank=True, auto_now=False, auto_now_add=False)



