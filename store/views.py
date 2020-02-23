from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import StoreForm,ProductForm
from .models import Store,Product
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'store/index.html')



class StoreView(LoginRequiredMixin,View):
	def get(self,request,*args,**kwargs):
		store = get_object_or_404(Store,owner=request.user)
		if not request.user.user_store:
			store_form = StoreForm()
			context = {
				'store_form': store_form,
				'store': store
			}
			return render(request,'store/store.html',context)
		else:
			context = {
				'store_form': None,
				'store': store
			}
			return render(request,'store/store.html',context)
	def post(self,request,*args,**kwargs):
		form = StoreForm(request.POST,request.FILES)
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
			return render(request,'store/store.html',context)

class EditStore(LoginRequiredMixin,View):
	def get(self,request,*args,**kwargs):
		store = get_object_or_404(Store,owner=request.user)

		store_form = StoreForm(instance=store)
		context = {
			'store_form': store_form,
			'store': store,
			'store_banner': store.banner
		}
		return render(request,'store/edit_store.html',context)

class MyProductView(LoginRequiredMixin,View):
	def get(self,request,*args,**kwargs):
		product_form = ProductForm()
		context = {
			'product_form': product_form
		}
		return render(request,'store/product.html',context)
	def post(self,request,*args,**kwargs):
		form = ProductForm(request.POST,request.FILES)
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
			return render(request,'store/product.html',context)



class CategoryProductView(View):
	def get(self,request,*args,**kwargs):
		return HttpResponse('okkkkkkkkkkkkkkkkkkk')


