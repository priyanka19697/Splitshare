from django.urls import path, include
from core.api.views import *
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'budgetowners', BudgetOwnerViewSet)
router.register(r'ExpenseCategories', ExpenseCategoryViewSet)
router.register(r'expenses', ExpenseViewSet)
router.register(r'defaultexpenses', DefaultExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
 ]
