from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Budget)
admin.site.register(BudgetOwner)
admin.site.register(ExpenseCategory)
admin.site.register(Expense)
admin.site.register(DefaultExpense)





