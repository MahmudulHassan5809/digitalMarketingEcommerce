from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from store.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages, auth
from .forms import CheckOutForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from .cart import Cart
from cart.models import Order, TransactionMethod


@login_required(login_url="auth:login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("store:home")


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


class CartDetail(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'cart/cart_detail.html')


class CartCheckOut(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email':     request.user.email,
            'address': request.user.user_profile.address,
            'country': request.user.user_profile.country,
            'state': request.user.user_profile.state,
            'zip_code': request.user.user_profile.zip_code,

        }
        checkout_form = CheckOutForm(initial=data)
        context = {
            'checkout_form': checkout_form
        }
        return render(request, 'cart/checkout.html', context)

    def post(self, request, *args, **kwargs):

        check_out_form = CheckOutForm(request.POST)

        if check_out_form.is_valid():
            cart = Cart(request)
            total_bill = 0.0
            for key, value in request.session['cart'].items():
                total_bill = total_bill + \
                    (float(value['price']) * value['quantity'])

            buyer = request.user
            payment_obj = get_object_or_404(
                TransactionMethod, id=int(request.POST['payment']))

            order = Order.objects.create(
                buyer=buyer, total_bill=total_bill, payment_method=payment_obj)

            for key, value in request.session['cart'].items():
                order.products.add(int(value['product_id']))

            product_count = ''
            for key, value in request.session['cart'].items():
                product_count += f"{value['name']} --> {value['quantity']}"

            order.product_count = product_count

            product_price = ''
            for key, value in request.session['cart'].items():
                price = (float(value['price']) * value['quantity'])
                product_price += f"{value['name']} --> {value['quantity']} : {price} "

            product_seller = ''
            for key, value in request.session['cart'].items():
                product_obj = get_object_or_404(
                    Product, id=int(value['product_id']))
                seller = product_obj.store.owner
                order.sellers.add(seller.id)
                product_seller += f"{value['name']} --> {product_obj.store.owner.username} "

            order.product_seller = product_seller
            order.product_price = product_price

            order.save()

            # cart.clear()

            messages.success(request, 'Your Order Has Been Submitted')
            return redirect('cart:cart_checkout')

        else:
            context = {
                'checkout_form': check_out_form
            }
            return render(request, 'cart/checkout.html', context)
