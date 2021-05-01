from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):

    categoryname = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryname
class Products(models.Model):
    productname = models.CharField(max_length = 100)
    price = models.FloatField()
    categoryname = models.ForeignKey('Category', on_delete=models.CASCADE)
    sku = models.CharField(max_length=10)

    def __str__(self):
        return self.productname

class CartProduct(models.Model):
    product = models.ForeignKey('Products',on_delete = models.CASCADE)
    qty = models.IntegerField()
    def __str__(self):
        return str(self.pk)



