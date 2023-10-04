from django import forms

class YourForm(forms.Form):
    item_name = forms.CharField(max_length=100)
    item_description = forms.CharField(widget=forms.Textarea)
    item_quantity = forms.IntegerField()
    item_price = forms.DecimalField(max_digits=10, decimal_places=2)
    departmentDropdown = forms.ChoiceField(choices=[
        ('option1', 'College of Arts and Sciences'),
        ('option2', 'College of Agriculture'),
        ('option3', 'College of Forestry'),
        ('option4', 'College of Hospitality Management and Tourism'),
        ('option5', 'College of Technology and Engineering'),
        ('option6', 'College of Education'),
        ('option7', 'Graduate School'),
    ])
    item_purpose = forms.CharField(widget=forms.Textarea)

