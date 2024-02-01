from django.db import models

# Create your models here.

class Bakery (models.Model):

    item = models.CharField(max_length=64)
    quantity = models.IntegerField()
    price = models.FloatField()
    #optional for image adding
    image = models.CharField(max_length=2083)