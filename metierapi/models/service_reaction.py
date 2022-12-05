from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractBaseUser, UserManager


class ServiceReaction(models.Model):

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    reaction = models.ForeignKey("Reaction", on_delete=models.CASCADE, related_name='service_reaction')
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name='service_comments')
