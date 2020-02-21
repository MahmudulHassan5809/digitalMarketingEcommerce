from django.contrib import admin
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('__str__',)
	search_fields = ('category_name',)
	list_per_page = 20
	

# Register your models here.
admin.site.register(Category , CategoryAdmin)