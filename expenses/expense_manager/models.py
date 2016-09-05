from django.db import models
from django.utils import timezone


class Portfolio(models.Model):
    class Meta:
        unique_together = (('first_name', 'last_name'),)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    started_working = models.DateField("Date of Hire", null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class ExpenseType(models.Model):
    name = models.CharField(max_length=255)
    is_haamasot_expense = models.BooleanField()

    def __str__(self):
        return self.name


class Expense(models.Model):
    portfolio = models.ForeignKey(Portfolio)
    expense_type = models.ForeignKey(ExpenseType)
    ammount = models.FloatField()
    date = models.DateField("Expense Date")

    def __str__(self):
        return self.expense_type.name + " Expense for " + self.portfolio.first_name + " " + self.portfolio.last_name + " - " + self.date.strftime("%d/%m/%y") + " - " + str(self.ammount) + "₪"
