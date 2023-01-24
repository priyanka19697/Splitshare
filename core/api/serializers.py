from django.contrib.auth.models import User
from ..models import *
from rest_framework import serializers

# serializers are used to define API representation
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'location', 'birth_date']

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model= Budget
        fields = '__all__'

class BudgetOwnerSerializer(serializers.ModelSerializer):

    budget = serializers.PrimaryKeyRelatedField(many=True, read_only = True)
    owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model =  BudgetOwner
        fields = ['budget', 'owner']
        depth = 1

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'
    
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
        depth = 1

class DefaultExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefaultExpense
        fields = '__all__'
        depth = 1


