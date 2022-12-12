from django.db import models

class Service(models.Model):

    creator = models.ForeignKey("MetierUser", on_delete=models.CASCADE, related_name='service_creator')
    service = models.CharField(max_length=50)
    image = models.CharField(max_length=50, null=True, blank=True)
    body = models.CharField(max_length=500, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE, related_name='service_comments', null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True, auto_now=True, auto_now_add=False)

    reactions = models.ManyToManyField("Reaction", through="ServiceReaction" )

    @property 
    def is_creator(self):
        return self.__creator

    @is_creator.setter
    def is_creator(self, value):
        self.__creator = value