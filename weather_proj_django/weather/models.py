from django.db import models

# Create your models here.

class CurrentLocation(models.Model):
    city_name = models.CharField(max_length=50)
    region = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    localtime = models.DateField()
    last_updated = models.DateField()
    temp_f = models.DecimalField(max_digits=5, decimal_places=2)
    condition = models.CharField(max_length=30)
    condition_img_url = models.CharField(max_length=100)

