from django.db import models

# Create your models here.
class Furniture(models.Model):
    furniture_types = (
        ('plastic','plastic'),
        ('wooden','wooden'),
        ('steel','steel')
    )
    Name = models.CharField(max_length=25)
    Price = models.IntegerField()
    Type = models.CharField(max_length=25,choices=furniture_types)
    Details = models.TextField()