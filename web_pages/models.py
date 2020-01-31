from django.db import models


# Create your models here.

class community_student(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    image = models.ImageField(upload_to='community_member')

    def __str__(self):
        return self.name
