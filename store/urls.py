from django.urls import path
from .views import (
	HomeView, 
	CategoryProductView, 
	StoreView, MyProductView, 
	EditStore, 
	MyProduct, 
	ProductDetailView,
	PaymenthMethodView,
	PaymenthMethodEdit,
	PaymenthMethodDelete
	)

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('product/category/<int:id>',
         CategoryProductView.as_view(), name="category_product"),
    path('store/view/', StoreView.as_view(), name="store_view"),
    path('store/my-product/', MyProductView.as_view(), name="product_view"),
    path('store/edit-store/<int:id>', EditStore.as_view(), name="edit_store"),
    path('store/my-product/<int:id>', MyProduct.as_view(), name="my_product"),
    path('store/product/detail/<int:pk>/',
         ProductDetailView.as_view(), name="product_detail"),

    path('store/payment/method/',
         PaymenthMethodView.as_view(), name="payment_method"),

    path('store/payment/method/edit/<int:id>',
         PaymenthMethodEdit.as_view(), name="payment_method_edit"),
    path('store/payment/method/delete/<int:id>',
         PaymenthMethodDelete.as_view(), name="payment_method_delete"),
]
