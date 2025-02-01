from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    pais  = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='', null=True)  
    price = models.DecimalField(max_digits=10, default=0, decimal_places=2)  
    f_vencimiento = models.DateField(null=True, blank=True)  # Fecha de vencimiento
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
