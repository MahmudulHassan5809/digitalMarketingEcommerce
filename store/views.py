from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import StoreForm, ProductForm
from .models import Store, Product, Category, WishList
from cart.models import Order
from django.views import View
from functools import reduce
from django.db import models
from django.db.models import Q
from django.views.generic import DetailView


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'store/index.html')


class StoreView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        store = Store.objects.filter(owner=request.user).first()
        if not store:
            store_form = StoreForm()
            context = {
                'store_form': store_form,
                'store': store,
                'edit_store': False
            }
            return render(request, 'store/store.html', context)
        else:
            store_form = StoreForm(instance=store)
            context = {
                'store_form': store_form,
                'store': store,
                'edit_store': True
            }
            return render(request, 'store/store.html', context)

    def post(self, request, *args, **kwargs):
        form = StoreForm(request.POST, request.FILES)
        context = {
            'store_form': form
        }
        if form.is_valid():
            store = form.save(commit=False)
            store.owner = request.user
            store.save()
            messages.success(request, 'Store is created successfully')
            return redirect('store:store_view')
        else:
            return render(request, 'store/store.html', context)


class EditStore(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        store = get_object_or_404(Store, pk=kwargs.get('id'))
        form = StoreForm(request.POST, request.FILES, instance=store)

        if form.is_valid():
            form.save()
            messages.success(request, 'Store Updated Successfully')
            return redirect('store:store_view')

        return redirect('store:store_view')


class MyProductView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        product_form = ProductForm()
        context = {
            'product_form': product_form
        }
        return render(request, 'store/product.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        context = {
            'product_form': form
        }
        if form.is_valid():
            product = form.save(commit=False)
            product.store = request.user.user_store
            product.save()

            taglist = request.POST.get("tags")

            tagslist = [str(r) for r in taglist.split(',')]
            product.tags.add(*tagslist)
            product.save()

            messages.success(request, 'Product is created successfully')
            return redirect('store:product_view')
        else:
            return render(request, 'store/product.html', context)


class MyProduct(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        store_id = kwargs.get('id')
        store_obj = get_object_or_404(Store, id=store_id)
        my_products = Product.objects.filter(store=store_id)

        page = request.GET.get('page', 1)
        paginator = Paginator(my_products, 10)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'my_products': products, "store": store_obj}
        return render(request, 'store/my_product.html', context)


class MyProductEdit(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        product_obj = get_object_or_404(Product, id=product_id)

        product_form = ProductForm(instance=product_obj)
        context = {
            'product_obj': product_obj,
            'product_form': product_form
        }

        return render(request, 'store/my_product_edit.html', context)

    def post(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        product_obj = get_object_or_404(Product, id=product_id)

        product_form = ProductForm(
            request.POST, request.FILES, instance=product_obj)

        context = {
            'product_form': product_form,
            'product_obj': product_obj
        }

        if product_form.is_valid():
            product_form.save()

            taglist = request.POST.get("tags")

            tagslist = [str(r) for r in taglist.split(',')]
            product_obj.tags.set(*tagslist, clear=False)
            product_obj.save()

            messages.success(request, 'Product Updated Successfully')
            return redirect('store:my_product', request.user.user_store.id)

        return render(request, 'store/my_product_edit.html', context)


class MyProductDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        instance = Product.objects.get(id=product_id)
        instance.delete()
        return redirect('store:my_product', request.user.user_store.id)


class CategoryProductView(View):
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('id')
        category_obj = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category_id)

        page = request.GET.get('page', 1)
        paginator = Paginator(products, 10)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'products': products, "category": category_obj}
        return render(request, 'store/category_product.html', context)


class ProductDetailView(DetailView):
    model = Product


class MySellDetails(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        store_id = kwargs.get('id')
        store_obj = get_object_or_404(Store, id=store_id)

        # all_products = store_obj.store_products.all()
        # product_ids = all_products.values_list('id', flat=True)

        sell_details = request.user.seller_orders.all()

        context = {
            'sell_details': sell_details,
            'store_obj': store_obj
        }
        return render(request, 'store/sell_details.html', context)


class MyBuyDetails(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('id')

        buy_details = request.user.buyer_orders.all()

        context = {
            'buy_details': buy_details,

        }
        return render(request, 'store/buy_details.html', context)


class TagProducts(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        tag_name = kwargs.get('tag_name')
        products = Product.objects.filter(tags__name__in=[tag_name])

        page = request.GET.get('page', 1)
        paginator = Paginator(products, 10)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'products': products, "tag_name": tag_name}
        return render(request, 'store/tag_product.html', context)


class ProductSearch(View):
    def post(self, request, *args, **kwargs):
        category_id = request.POST.get('category')
        search = request.POST.get('search')

        category_obj = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(Q(category__category_name__icontains=search) | Q(
            name__icontains=search) | Q(description__icontains=search), category=category_id)

        page = request.GET.get('page', 1)
        paginator = Paginator(products, 10)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'products': products,
                   "category_obj": category_obj, "search": search}
        return render(request, 'store/search_product.html', context)


class AddProductWishlist(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('id')
        product_obj = get_object_or_404(Product, id=product_id)

        wishlist_check = WishList.objects.filter(
            owner=request.user, product=product_obj).first()

        if wishlist_check:
            messages.success(request, "Product Already In Your WishList")
        else:
            add_wishlist = WishList.objects.create(
                owner=request.user, product=product_obj)
            messages.success(request, "Product Added To Your WishList")

        return redirect('store:wishlist')


class MyWishList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        my_products = WishList.objects.filter(owner=request.user)

        page = request.GET.get('page', 1)
        paginator = Paginator(my_products, 10)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'my_products': products}
        return render(request, 'store/my_wishlist.html', context)


class RemoveFromWishList(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        wishlist_id = kwargs.get('id')
        instance = WishList.objects.get(id=wishlist_id)
        instance.delete()
        messages.success(request, "Product Deleted From Your WishList")
        return redirect('store:wishlist')
