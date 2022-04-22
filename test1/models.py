from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=10)
    image = models.ImageField()
    description = models.TextField()
    data = models.DateField()


class Stories(models.Model):
    image = models.ImageField()