from django.shortcuts import get_object_or_404
from .serializers import UserSerializer,User

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class SignupView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=request.data['email'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data})
        return Response(serializer.errors)

class SignInView(APIView):
    def post(self,request):
        user = get_object_or_404(User, email= request.data['email'])
        if not user.check_password(request.data['password']):
            return Response({"invalid password"})
        serializer = UserSerializer(instance=user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'data': serializer.data})