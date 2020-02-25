from django.forms import ModelForm 
from .models import Store,Product,PaymentMethod


class StoreForm(ModelForm):
	class Meta:
		model = Store 
		fields = ['store_name','banner']



class ProductForm(ModelForm):
	class Meta:
		model = Product 
		exclude = ['store']


class PaymentMethodForm(ModelForm):
	class Meta:
		model = PaymentMethod 
		exclude = ['store']