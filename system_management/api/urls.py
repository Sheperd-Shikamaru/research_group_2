from django.urls import path
from system_management.api.views import login_api

urlpatterns = [
    path('login_api/', login_api, name='login_api')
]