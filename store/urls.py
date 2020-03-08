from django.urls import path
from .views import (
    HomeView,
    CategoryProductView,
    StoreView, MyProductView,
    EditStore,
    MyProduct,
    ProductDetailView,
    MySellDetails,
    MyBuyDetails,
    MyProductEdit,
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
    path('store/my-product/edit/<int:id>',
         MyProductEdit.as_view(), name="my_product_edit"),
    path('store/product/detail/<int:pk>/',
         ProductDetailView.as_view(), name="product_detail"),

    path('store/my-sell/details/<int:id>/',
         MySellDetails.as_view(), name="my_sell_details"),
    path('store/my-buy/details/<int:id>/',
         MyBuyDetails.as_view(), name="my_buy_details"),


]
