from django.shortcuts import render
import json
from django.urls import reverse
from django.http import JsonResponse
import requests

def host_url(request):
    url = request.build_absolute_uri()
    index = url.index("system_management")
    url = url[0:index - 1]
    return url

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def login(request):
    """User login function with API."""
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        # Form data send using AJAX.
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        # URL for the login API.
        url = f"{host_url(request)}{reverse('login_api')}"
        # Payload containing the fields for the API.
        payload = json.dumps({
            "username": username,
            "password": password
        })
        # API header for the type of data format of the payload.
        headers = {
            'Content-Type': 'application/json',
        } 
        # Request to the API with method POST using requests library.
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=120)
            response_data = json.loads(response.json())

            return JsonResponse(data=response_data, safe=False)
        except requests.exceptions.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
               
    return render(request, 'login.html')  
