from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='buyer_orders')
    sellers = models.ManyToManyField(User, related_name='seller_orders')
    products = models.ManyToManyField(Product, related_name='product_orders')
    product_count = models.CharField(max_length=255)
    product_price = models.CharField(max_length=255)
    product_seller = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    total_bill = models.FloatField()
    paid = models.BooleanField(default=False)
    payment_method = models.ForeignKey(
        "TransactionMethod", on_delete=models.CASCADE, related_name='payment_method_order')

    def ordered_products(self):
        return ",".join([str(p) for p in self.products.all()])

    def product_sellers(self):
        return ",".join([str(p) for p in self.sellers.all()])


class TransactionMethod(models.Model):
    method_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to="payment_methods/")
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.method_name}-{self.account_number}'
