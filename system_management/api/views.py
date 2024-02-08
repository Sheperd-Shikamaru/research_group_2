from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
import json
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST'])
@permission_classes([AllowAny])
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')
    try:
        response_data = json.dumps({
            "username": username,
            "password": password
        })
        user = authenticate(username=username, password=password)
        if not user:
                data = {'error': "Invalid Credentials"}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        user_id = user.id
        response_data = json.dumps({
            'user_id':user_id,
            'token': token.key, 
            "status":"success",
            })
        return Response(response_data, status=status.HTTP_200_OK)
        # else:
        #     return Response(status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)