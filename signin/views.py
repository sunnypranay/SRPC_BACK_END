# this login will use Django rest framework to authenticate users
# and assign them a jwt token and return it to the user
# this will be used to authenticate users for the rest of the app
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request, *args, **kwargs):
        try:
            email = request.data['email']
            password = request.data['password']
        except:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        if not email or not password:
            return Response({'error': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if not user:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_404_NOT_FOUND)
        
        token = TokenObtainPairSerializer.get_token(user)
        return Response({'token': str(token.access_token), 'user_id': user.id, 'email': user.email}, status=status.HTTP_200_OK)