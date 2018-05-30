# -*- coding: utf-8 -*-class A(models.Model):
    # fields'n'stuff

from django.forms.models import models

class FundamentalDataModel(models.Model):
    

    class TransientFundamentalDataModel(FundamentalDataModel):
        def save(*args, **kwargs):
            pass  # avoid exceptions if called

    class Meta:
        abstract = True  # no table created
        managed = False
