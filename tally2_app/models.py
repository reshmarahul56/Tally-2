from django.db import models


class Costcentr(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    emply=models.CharField(max_length=225)

class GroupModel(models.Model):
    name =  models.CharField(max_length=225,default="Null",blank=True)
    alias =  models.CharField(max_length=225,default="Null",blank=True)
    under =models.CharField(max_length=225,default="Null",blank=True)
    nature_of_group = models.CharField(max_length=225,default="Null",blank=True)
    does_it_affect =models.CharField(max_length=225,default="Null",blank=True)
    gp_behaves_like_sub_ledger =  models.CharField(max_length=225,default="Null",blank=True)
    nett_debit_credit_bal_reporting =  models.CharField(max_length=225,default="Null",blank=True)
    used_for_calculation =  models.CharField(max_length=225,default="Null",blank=True)
    method_to_allocate_usd_purchase =  models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.name

class GrpAlter(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    nature=models.CharField(max_length=225)
    grp=models.CharField(max_length=225)
    nett=models.CharField(max_length=225)
    used=models.CharField(max_length=225)
    method=models.CharField(max_length=225)