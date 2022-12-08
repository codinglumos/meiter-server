from django.db import models
from django.contrib.auth.models import User


class ServiceReaction(models.Model):

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.ForeignKey("Reaction", on_delete=models.CASCADE, related_name='service_reaction')
    service = models.ForeignKey("Service", on_delete=models.CASCADE, related_name='service_comments')
