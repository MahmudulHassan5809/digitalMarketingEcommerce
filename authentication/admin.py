from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
	list_display = ["profile_name","phone_number","address","user_email","profile_pic"]
	search_fields = ('user_id__username','phone_number')
	list_filter = ['phone_number','user__email']
	list_per_page = 20


	def profile_name(self,obj):
		return obj.user.username

	def user_email(self,obj):
		return obj.user.email

admin.site.register(Profile,ProfileAdmin)