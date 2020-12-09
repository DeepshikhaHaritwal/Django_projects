from django.contrib import admin
from .models import income_details, expense_details
# Register your models here.
admin.site.register(income_details)
admin.site.register(expense_details)