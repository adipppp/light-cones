from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    rarity = models.IntegerField()
    path = models.CharField(max_length=255)
