from django.db import models

# Create your models here.
class income_details(models.Model):
    budget = models.IntegerField()
    income_source = models.CharField(max_length=50)
    income_amount = models.IntegerField()
    income_date = models.DateField()

class expense_details(models.Model):
    estimated_expenses = models.IntegerField()
    expense_source = models.CharField(max_length=50)
    expense_amount = models.IntegerField()
    expense_date= models.DateField()

def __str__(self):
    return self.income_source

class Meta:
     db_table='MyExpenseTracker_income_details'
