from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=60, unique=True, null=False, blank=False)


class Brand(models.Model):
    brand_name = models.CharField(max_length=60, unique=True, null=False, blank=False)


class Item(models.Model):
    item_name = models.CharField(max_length=60, null=False, blank=False)
    item_quantity = models.IntegerField(null=False, blank=False)
    item_image = models.ImageField(upload_to='pictures', max_length=255, null=True, blank=True)
    item_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    item_brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

class Order(models.Model):
    order_item = models.ForeignKey('Item', on_delete=models.CASCADE)
    order_user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
