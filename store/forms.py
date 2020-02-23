from django.forms import ModelForm 
from .models import Store,Product


class StoreForm(ModelForm):
	class Meta:
		model = Store 
		fields = ['store_name','banner']



class ProductForm(ModelForm):
	class Meta:
		model = Product 
		exclude = ['store']