# Create your models here.

from mongoengine import *
import datetime
 
connect('wealth_management_indices')
 
class ind_nifty100list(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)

class nifty_500_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)
        
class nifty_200_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)

class nifty_100_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)
        
class nifty_50_companies(Document):
		Company_Name = StringField(max_length=100,required=False)
		Industry = StringField(max_length=100,required=True)
		Symbol = StringField(max_length=100,required=True)
		Series = StringField(max_length=100,required=True)
		ISIN_Code = StringField(max_length=100,required=False)

class nift100data(Document):
        Date = DateTimeField(default=datetime.datetime.utcnow)
        Open = DecimalField(max_length=100,required=True)
        High = DecimalField(max_length=100,required=True)
        Low =  DecimalField(max_length=100,required=True)
        Close =DecimalField(max_length=100,required=True)
        Shares_Traded =DecimalField(required=False)
        Turnover_in_CR = StringField(required=False)

