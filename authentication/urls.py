from django.urls import path
from .views import RegisterView,LoginView,DashboardView,EditProfileView

app_name = 'auth'

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('dashboard/', DashboardView.as_view(), name="dashboard"),
    path('edit/profile', EditProfileView.as_view(), name="edit_profile"),
]
