from django.db import models
from django.contrib.auth.models import User
from store.models import Product


class Order(models.Model):
	customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_orders')
	products = models.ManyToManyField(Product, related_name='product_orders')
	product_count = models.CharField(max_length=255)
	product_price = models.CharField(max_length=255)
	completed = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)
	total_bill = models.FloatField()
	paid = models.BooleanField(default=False)
	
	def ordered_products(self):
		return ",".join([str(p) for p in self.products.all()])

		

	

