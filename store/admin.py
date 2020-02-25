from django.contrib import admin
from .models import Category, Store, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('category_name',)
    list_per_page = 20


# Register your models here.
admin.site.register(Category, CategoryAdmin)


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'owner', 'active', 'banner')
    list_filter = ('owner', 'active')
    search_fields = ('store_name', 'owner')
    list_per_page = 20
    list_editable = ('active',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'store',
                    'get_owner', 'discount', 'image')
    raw_id_fields = ('store',)
    list_filter = ('category', 'store')
    search_fields = ('name', 'store',)
    list_per_page = 20

    def get_owner(self, obj):
        return obj.store.owner.username
