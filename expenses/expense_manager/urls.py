from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'addExpense/$', views.expense_form, name='expensesForm'),
    url(r'uploadFile/$', views.file_upload, name='uploadFile'),
    url(r'listExpense/$', views.view_expenses, name='expenseList'),
    url(r'addFile/$', views.add_file, name='addFile')
]