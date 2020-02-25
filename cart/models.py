from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_orders')
    products = models.ManyToManyField(
        Product, related_name='product_orders')
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField()
    bill = models.FloatField()
