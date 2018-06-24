from django import forms
from .models import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget

class mutualfund_form(forms.ModelForm):
     def __init__(self, *args, **kwargs):
        super(mutualfund_form, self).__init__(*args, **kwargs)
        self.fields['Company_Name'].label = "Company Name"
        #self.fields['Company_Name'].widget.attrs["onchange"]="javascript:companynamechange(this);"
        self.fields['Scheme_Name'].label = "Scheme Name"
        self.fields['Company_Name'].widget.attrs["style"]="width: 266px;margin-left: 1px;margin-right: 91px;"
        self.fields['Company_Name'].widget.attrs["name"]="Company_Name"
        self.fields['Company_Name'].widget.attrs["id"]="Id_Company_Name"
        self.fields['Scheme_Name'].widget.attrs["style"]="width: 266px;margin-left: 1px;margin-right: 91px;"
        self.fields['Scheme_Name'].widget.attrs["name"]="Scheme_Name"
        self.fields['Scheme_Name'].widget.attrs["id"]="Id_Scheme_Name"
        self.fields['Scheme_Name'].required = False
        #self.fields['backdate'].widget.attrs["style"]="width: 100px;margin-left: 45px;margin-right: 91px;"
        #self.fields['companyName'].widget.attrs["onchange"]="javascript:change(this);"
        
     class Meta():
        model= mutualfund_company_schema
        fields= ['Company_Name','Scheme_Name']
        
        