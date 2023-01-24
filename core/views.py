from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from core.serializers import UserSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hello world. You are at buddy index")

# Viewsets define view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


