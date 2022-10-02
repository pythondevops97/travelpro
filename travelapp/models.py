from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=25)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
class teams(models.Model):
    name = models.CharField(max_length=15)
    img = models.ImageField(upload_to='pics')
    decs = models.TextField()
