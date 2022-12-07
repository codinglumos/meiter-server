from django.db import models
from django.contrib.auth.models import User


class Service(models.Model):

    creator = models.ForeignKey("Creator", on_delete=models.CASCADE, related_name='service_creator')
    service = models.CharField(max_length=50)
    image = models.CharField(max_length=50, null=True, blank=True)
    body = models.CharField(max_length=500, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name='service_comments', null=True, blank=True)
    