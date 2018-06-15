from django import forms
from .models import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

class strategy_form(forms.ModelForm):
    
     def __init__(self, *args, **kwargs):
        super(strategy_form, self).__init__(*args, **kwargs)
        self.fields['companyName'].label = "Company Name"
        self.fields['backdate'].label = "Backdate"
        self.fields['backdate'].widget.attrs["name"]="Backdate"
        BIRTH_YEAR_CHOICES = ('2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018')
        self.fields['backdate']=forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
        self.fields['companyName'].widget.attrs["style"]="width: 266px;margin-left: 1px;margin-right: 91px;"
        self.fields['companyName'].widget.attrs["name"]="companyName"
        #self.fields['backdate'].widget.attrs["style"]="width: 100px;margin-left: 45px;margin-right: 91px;"
        #self.fields['companyName'].widget.attrs["onchange"]="javascript:change(this);"
        
     class Meta():
        model= strategy
        fields= ['companyName','backdate']