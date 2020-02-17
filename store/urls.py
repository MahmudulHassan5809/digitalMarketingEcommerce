from django.urls import path
from .views import (HomeView)

app_name = 'store'

urlpatterns = [
    path('', HomeView.as_view(), name="home")
]
