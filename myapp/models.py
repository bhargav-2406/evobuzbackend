from django.db import models
from django.contrib.postgres.fields import ArrayField

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Business_name = models.CharField(max_length=255)
    product_img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    

    def __str__(self):
        return self.product_name

class Services(models.Model):
    description_ser = models.CharField(max_length = 300)
    highestAmount = models.DecimalField(max_digits = 10)
    location = models.CharField()
    lowestAmount = models.DecimalField(max_digits = 10)
    serviceCategory = models.CharField(max_length = 50)
    serviceName = models.CharField(max_length = 50)
    selectedEventTypes = ArrayField(models.CharField(max_length = 50))
    selectedServices = ArrayField(models.CharField(max_length=200))
    images = models.ImageField(upload_to='./media')
    videos = models.FileField(upload_to='./media')

    def __str__(self):
        return self.serviceName


