from django.contrib import admin

from . import models
admin.site.register(models.Expense)
admin.site.register(models.ExpenseType)
admin.site.register(models.Portfolio)

print("This is home")
print("This is adding")