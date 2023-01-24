from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from core.api.serializers import *

# Create your views here.

def index(request):
    return HttpResponse("Hello world. You are at buddy index")





