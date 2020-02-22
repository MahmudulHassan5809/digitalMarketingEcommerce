from django.shortcuts import render,HttpResponse
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'store/index.html')


class CategoryProductView(View):
	def get(self,request,*args,**kwargs):
		return HttpResponse('okkkkkkkkkkkkkkkkkkk')