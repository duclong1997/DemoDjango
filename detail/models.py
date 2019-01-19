from django.db import models

# Create your models here.
# create table have name = name of class in models
class post(models.Model):
    #  create column in table
    title  = models.CharField(max_length=100)
    numberPost =models.IntegerField(default=0)
    datetime = models.DateField(auto_now_add=True)
    body=models.TextField()