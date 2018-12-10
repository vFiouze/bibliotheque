# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from bibliothequeapp.models import Loan, Member
import pdb
from datetime import date
from django.core.paginator import Paginator

# Create your views here.

@login_required
def app(request):
    template = loader.get_template('app/app.html')
    userFirstName = request.user.first_name
    context = {"first_name":userFirstName}
    return HttpResponse(template.render(context,request))


@login_required
def liste(request):
    member = ""
    actif = 0
    params =  {}
    if "name" in request.GET:
        params["LOAN_MEMBER_ID"]=request.GET["name"]
    if "actif" in request.GET:
        params["LOAN_END_EFFECTIVE_DATE__gt"]=date.today()
    res = Loan.objects.filter(**params).values()
    p = Paginator(res,10)
    if "page" in request.GET:
        page=request.GET["page"]
    else:
        page = 1
    ret = p.page(page)
    ran = []
    for i in p.page_range:
        ran.append(i)
    return JsonResponse({"result":"OK", "data" : list(ret),"range" : ran})

def searchmember(request):
    member=request.GET["member"]
    param = {"MEMBER_ID__startswith":str(member)}
    res = Member.objects.filter(**param).values()
    return JsonResponse({"result":"OK", "data" : list(res)})