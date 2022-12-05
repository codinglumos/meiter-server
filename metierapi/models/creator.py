from django.db import models
from django.contrib.auth.models import User


class Creator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="creator")
    bio = models.CharField(max_length=155)
    profile_image = models.CharField(max_length=50, null=True, blank=True)


    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    