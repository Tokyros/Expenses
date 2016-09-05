from django import forms
from functools import partial
import openpyxl

from . import models


class NewExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = ['portfolio', 'expense_type', 'ammount', 'date']

    def __init__(self, *args, **kwargs):
        super(NewExpenseForm, self).__init__(*args, **kwargs)
        self.fields['portfolio'].widget.attrs.update({'class': 'w3-input w3-border w3-light-grey'})
        self.fields['expense_type'].widget.attrs.update({'class': 'w3-input w3-border w3-light-grey'})
        self.fields['ammount'].widget.attrs.update({'class': 'w3-input w3-border w3-light-grey'})
        self.fields['date'].widget.attrs.update({'class': 'w3-input w3-border w3-light-grey', 'type': 'date'})


class UploadFileForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data['file']
        try:
            openpyxl.load_workbook(file)
        except:
            raise forms.ValidationError("Not an excel file")