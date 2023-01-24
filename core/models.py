from django.db import models
from django.contrib.auth.models import User
from core.buddy_constants import TimePeriods
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Budget(models.Model):
    name = models.CharField(max_length=150)
    start_date = models.DateTimeField()
    period = models.CharField(
        max_length=10,
        choices=[(tag, tag.value) for tag in TimePeriods],  # Choices is a list of Tuple 
        default=TimePeriods.MONTHLY)

class BudgetOwner(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=200) # rent, insurance, misc 
    is_planned = models.BooleanField(default=True)

class Expense(models.Model):
    amount = models.IntegerField()
    is_expense = models.BooleanField()
    category = models.ForeignKey(ExpenseCategory, on_delete=models.DO_NOTHING)
    
class DefaultExpense(models.Model):
    expense = models.ForeignKey(Expense, on_delete=models.DO_NOTHING)






