from django.db import models


# Create your models here.

class Card(models.Model):
    suit = models.CharField(max_length=1)
    rank = models.CharField(max_length=1)
    value = models.IntegerField(default=0)
    img_url = models.CharField(max_length=200)
