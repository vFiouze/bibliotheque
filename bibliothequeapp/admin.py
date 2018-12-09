# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Person,Member,Author,Document,Document_Type,Loan

admin.site.register(Person)
admin.site.register(Member)
admin.site.register(Author)
admin.site.register(Document)
admin.site.register(Document_Type)
admin.site.register(Loan)
