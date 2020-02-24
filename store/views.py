from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import StoreForm, ProductForm
from .models import Store, Product,Category
from django.views import View


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
            messages.success(request, 'Product is created successfully')
            return redirect('store:product_view')
        else:
            return render(request, 'store/product.html', context)


class MyProduct(LoginRequiredMixin,View):
    def get(self,request,*args,**kwargs):
        store_id = kwargs.get('id')
        store_obj = get_object_or_404(Store,id=store_id)
        my_products = Product.objects.filter(store=store_id)
        
        page = request.GET.get('page', 1)
        paginator = Paginator(my_products, 10)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'my_products' : products,"store":store_obj}
        return render(request, 'store/my_product.html', context)



class CategoryProductView(View):
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('id')
        category_obj = get_object_or_404(Category,id=category_id)
        products = Product.objects.filter(category=category_id)

        page = request.GET.get('page', 1)
        paginator = Paginator(products, 10)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        context = {'products' : products,"category":category_obj}
        return render(request, 'store/category_product.html', context)
