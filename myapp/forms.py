from django import forms
from .models import Category, Transaction
#from .models import Transaction

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"
