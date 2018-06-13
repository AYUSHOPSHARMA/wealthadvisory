from django import forms
from .models import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget


class strategy_form(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(strategy_form, self).__init__(*args, **kwargs)
        self.fields['companyName'].label = "Company Name"
        self.fields['backdate'].label = "backdate"
        self.fields['backdate']=DateField(widget=AdminDateWidget)
        
    class Meta():
        model= strategy
        fields= ['companyName','backdate']