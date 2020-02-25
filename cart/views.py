from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from store.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages, auth
from django.views.decorators.http import require_POST
from .cart import Cart
from cart.models import Order


@login_required(login_url="auth:login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("store:home")


@login_required(login_url="auth:login")
def cart_detail(request):
    sub = []
    qty = []
    total = 0
    for key, value in request.session['cart'].items():
        sub.append(float(value['price']) * float(value['quantity']))
        qty.append(int(value['quantity']))
    for s in sub:
        total = total + s
    context = {
        'title': 'My Cart',
        'sub': sub,
        'total': total
    }
    return render(request, 'cart/cart_detail.html', context)


@login_required(login_url="auth:login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart:cart_detail")


@login_required(login_url="auth:login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart:cart_detail")


@login_required(login_url="auth:login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart:cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart:cart_detail")



class CartDetail(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        return render(request,'cart/cart_detail.html')