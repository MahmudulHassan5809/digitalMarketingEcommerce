from django.forms import ModelForm 
from .models import Store 


class StoreForm(ModelForm):
	class Meta:
		model = Store 
		fields = ['store_name','banner']