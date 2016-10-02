from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Book(models.Model):
    title=models.CharField(max_length=100)
    auther=models.CharField(max_length=30 ,blank=True, null=True)
    publisher = models.CharField(max_length=30,blank=True , null=True)
    number_of_reviews = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)
    def __str__(self):
        return self.title

class Review(models.Model):
    review=models.CharField(max_length=2000)
    star_rating = models.IntegerField(default=0)
    book=models.CharField(max_length=50 , null=True)
    review_by=models.OneToOneField(User , null=True)
    datetime = models.DateTimeField(default=timezone.now)

