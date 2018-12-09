# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    PERSON_ID          = models.CharField(max_length=9,primary_key=True)
    PERSON_NAME        = models.CharField(max_length=50,blank=False)
    PERSON_LAST_NAME   = models.CharField(max_length=50,blank=False)
    PERSON_DT_BIRTH    = models.DateField(blank=False)
    PERSON_STREET_NAME = models.CharField(max_length=50,blank=False)
    PERSON_ZIP_CODE    = models.CharField(max_length=5,blank=False)
    PERSON_CITY        = models.CharField(max_length=20,blank=False)
    PERSON_COUNTRY     = models.CharField(max_length=20,blank=False)
    class Meta():
        db_table = 'PERSON'
    
class Member(models.Model):
    MEMBER_ID        = models.ForeignKey(Person,on_delete=models.PROTECT,primary_key=True)
    MEMBER_DT_JOIN   = models.DateField(blank=False)
    MEMBER_IS_ACTIVE = models.BooleanField(null=False)
    class Meta():
        db_table = 'MEMBER'
    
class Author(models.Model):
    AUTHOR_ID        = models.CharField(max_length=10,primary_key=True)
    AUTHOR_NAME      = models.CharField(max_length=50,blank=False)
    AUTHOR_LAST_NAME = models.CharField(max_length=50,blank=False)
    class Meta():
        db_table = 'AUTHOR'
    
class Document_Type(models.Model):
    DOCUMENT_TYPE_ID   = models.CharField(max_length=2,primary_key=True)
    DOCUMENT_TYPE_DESC = models.CharField(max_length=50,blank=False)
    class Meta():
        db_table = 'DOCUMENT_TYPE'
    
class Document(models.Model):
    DOCUMENT_ID          = models.CharField(max_length=9,primary_key=True)
    DOCUMENT_TYPE        = models.ForeignKey(Document_Type,on_delete=models.PROTECT)
    DOCUMENT_AUTHOR_TYPE = models.ForeignKey(Author,on_delete=models.PROTECT)
    class Meta():
        db_table = 'DOCUMENT'
        
class Loan(models.Model):
    LOAN_ID                 = models.CharField(max_length=9,primary_key=True)
    LOAN_ORDINAL            = models.IntegerField(default=1)
    LOAN_MEMBER_ID          = models.ForeignKey(Member,on_delete=models.PROTECT)
    LOAN_START_DATE         = models.DateField(auto_now_add=True)
    LOAN_END_PREDICT_DATE   = models.DateField()
    LOAN_END_EFFECTIVE_DATE = models.DateField()
    LOAN_DOCUMENT_ID        = models.ForeignKey(Document,on_delete=models.PROTECT)
    LOAN_IS_EXTENDED        = models.BooleanField(null=False)
    
    class Meta:
        db_table = 'LOAN'          
        unique_together=(('LOAN_ID','LOAN_ORDINAL'),)        