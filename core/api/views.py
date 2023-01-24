
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from ..models import *
from rest_framework import viewsets, permissions
from core.api.serializers import *

# Viewsets define view behavior
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_class = [permissions.IsAuthenticated]

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_class = [permissions.IsAuthenticated]

class BudgetOwnerViewSet(viewsets.ModelViewSet):
    queryset = BudgetOwner.objects.all()
    serializer_class = BudgetOwnerSerializer
    permission_class = [permissions.IsAuthenticated]   

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    permission_class = [permissions.IsAuthenticated]   

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_class = [permissions.IsAuthenticated]   

class DefaultExpenseViewSet(viewsets.ModelViewSet):
    queryset = DefaultExpense.objects.all()
    serializer_class = DefaultExpenseSerializer
    permission_class = [permissions.IsAuthenticated]   