from django.db import models
from django.contrib.auth.models import User


class Favorite(models.Model):

    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name='favorited')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favoritor')