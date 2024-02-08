from django.urls import path
from system_management.views import login

urlpatterns = [
    path('login/', login, name='login')
]