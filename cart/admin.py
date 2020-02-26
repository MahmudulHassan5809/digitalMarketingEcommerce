from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
	list_display = ["customer","completed","ordered_products","product_count","product_price","total_bill","paid"]
	search_fields = ('customer','completed',)
	list_filter = ['completed','paid']
	list_editable = ['completed','paid']
	list_per_page = 20



admin.site.register(Order,OrderAdmin)