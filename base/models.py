from django.db import models
from django.contrib import admin
from django.dispatch import receiver

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=25, unique=True)
    description = models.CharField(max_length=250)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=4, default=0.00)
    display_price = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super(Product, self).delete(*args, **kwargs)

    def __str__(self):
        return self.product_id + self.description