import openpyxl
import datetime
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.contrib import messages
from . import forms
from . import models
import pandas
import bs4


def index(request):
    return render(request, 'expense_manager/expense_manager_base_layout.html')


def view_expenses(request):
    expenses = models.Expense.objects.all()
    portfolios = models.Portfolio.objects.all()
    data = []
    for expense in expenses:
        expense_fields_dict = {'portfolio': expense.portfolio.first_name + " " + expense.portfolio.last_name, 'expense_type': expense.expense_type.name, 'ammount': expense.ammount, 'date': expense.date}
        data.append(expense_fields_dict)
    table = pandas.DataFrame(data=data)[['portfolio', 'date', 'expense_type', 'ammount']].to_html(index=False, classes='myTable')
    beautifulSoupTable = bs4.BeautifulSoup(table)
    beautifulSoupTable.find('table')['class'] = 'pure-table w3-animate-top'
    beautifulSoupTable.find('table')['id'] = 'myTable'
    beautifulSoupTable = str(beautifulSoupTable)
    return render(request, 'expense_manager/expense_list.html', {'table': beautifulSoupTable, 'portfolios': portfolios})


@login_required
def expense_form(request):
    form = forms.NewExpenseForm()

    if request.method == 'POST':
        form = forms.NewExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense Added")
            return HttpResponseRedirect(reverse('expensesForm'))
    return render(request, 'expense_manager/expense_form.html', {'form': form})


@login_required
def add_file(request):
    #Comment Attempt
    form = forms.UploadFileForm()
    if request.method == 'POST':
        form = forms.UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        create_expenses_from_file(request.FILES['file'])
        messages.success(request, "File Added")
        return HttpResponseRedirect(reverse('expensesForm'))
    return render(request, 'expense_manager/add_file.html', {'form': form})


def create_expenses_from_file(file):
    wb = openpyxl.load_workbook(file)
    for sheet in wb.worksheets:
        for row in sheet.iter_rows("A2:C99"):
            if row[0].value:
                print(row[0].value)
                portfolio_first_name, portfolio_last_name = row[0].value.split(" ")
                date = datetime.datetime.strptime(row[1].value, '%m/%d/%y')
                ammount = float(row[2].value)

                portfolio, created = models.Portfolio.objects.get_or_create(first_name=portfolio_first_name, last_name=portfolio_last_name)

                expense_type, created = models.ExpenseType.objects.get_or_create(name=sheet.title, is_haamasot_expense=True)

                expense, created = models.Expense.objects.get_or_create(portfolio=portfolio, expense_type=expense_type, ammount=ammount, date=date)

                print(expense)


