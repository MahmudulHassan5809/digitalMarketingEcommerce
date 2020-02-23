from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StoreForm
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'store/index.html')



class StoreView(LoginRequiredMixin,View):
	def get(self,request,*args,**kwargs):
		store_form = StoreForm()
		context = {
			'store_form': store_form
		}
		return render(request,'store/store.html',context)
	def post(self,request,*args,**kwargs):
		form = StoreForm(request.POST)
		if form.is_valid():
			store = form.save(commit=False)
			store.owner = request.user
			store.save()
			return redirect('store:store_view')
		else:
			return redirect('store:store_view')





class CategoryProductView(View):
	def get(self,request,*args,**kwargs):
		return HttpResponse('okkkkkkkkkkkkkkkkkkk')


