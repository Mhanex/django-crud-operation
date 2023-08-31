from django import forms
from crud.models import Employee


class CreateEmployeeForm(forms.ModelForm):
    
    class Meta:

        model = Employee
        fields = ['first_name','last_name','email','phone','address','city','province','country']

class UpdateEmployeeForm(forms.ModelForm):
    
    class Meta:

        model = Employee
        fields = ['first_name','last_name','email','phone','address','city','province','country']