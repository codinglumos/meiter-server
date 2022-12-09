from django.db import models
from django.contrib.auth.models import User


class MetierCustomer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=50, null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
