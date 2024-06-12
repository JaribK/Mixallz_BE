from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from .models import Users
from .serializers import UserSerializer
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from users.models import Users

class UsersList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = Users.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(testLocation=location)
        return queryset
    
class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = Users.objects.all()