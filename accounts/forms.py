# forms.py

from django import forms

class PurchaseRequestForm(forms.Form):
    department = forms.CharField(max_length=100)
    purpose = forms.CharField(widget=forms.Textarea)
    item_name = forms.CharField(max_length=100)
    item_description = forms.CharField(widget=forms.Textarea)
    item_unit = forms.CharField(max_length=50)
    item_quantity = forms.IntegerField()
    item_price = forms.DecimalField(max_digits=10, decimal_places=2)


