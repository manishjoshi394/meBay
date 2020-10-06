from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Listing(models.Model):
    ''' 1. Title of listing
        2. Text based description
        3. Starting bid
        4. Image URL
        5. Category: fashion/toys/electronics/furniture etc.'''
    title = models.CharField(max_length=30)
    desciption = models.TextField()
    bid = models.IntegerField()
    imgurl = models.URLField()
    category = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title} for {self.bid} INR"

class Bid(models.Model):
    pass

class Comment():
    pass