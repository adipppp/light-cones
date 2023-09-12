from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    rarity = models.IntegerField()
    path = models.CharField(max_length=255)

