from django.db import models

# Create your models here.
class product(models.Model):
    nameproduct= models.TextField()
    price = models.FloatField(default=0.0)
    detail = models.CharField(max_length=100)