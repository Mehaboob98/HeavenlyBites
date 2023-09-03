from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  
    description = models.TextField()
    steps = models.TextField()

    def __str__(self):
        return self.title

