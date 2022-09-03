from django.shortcuts import render
from django.contrib import messages
from multiprocessing import context
from unicodedata import name
from django.http import JsonResponse
from django.shortcuts import render, redirect

from .models import *
from datetime import datetime, date, timedelta
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def costcentr(request):
    centr=Costcentr.objects.all()
    context={'centr':centr,}

    return render(request, 'costcentr.html',context)
def centr(request,pk):
    centr=Costcentr.objects.get(id=pk)
    return render(request, 'update_costcentr.html',{'i':centr})


def update_centr(request,pk):
    if request.method=='POST':
        centr =Costcentr.objects.get(id=pk)
        centr.name = request.POST.get('name')
        centr.alias = request.POST.get('alias')
        centr.under = request.POST.get('under')
        centr.emply = request.POST.get('emply')
        
        
        centr.save()
        return redirect('costcentr')
    return render(request, 'update_costcentr.html',)

@csrf_exempt
def create_group(request):
    if request.method == 'POST':
        gname = request.POST['gname']
        alia = request.POST['alia']
        if len(gname) <= 0:
            return JsonResponse({
                'status': 00
            })

        if len(alia) <= 0:
            alia = None
        else:
            pass

        under = request.POST['und']
        gp = request.POST['subled']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']

        mdl = GroupModel(
            name=gname,
            alias=alia,
            under=under,
            gp_behaves_like_sub_ledger=gp,
            nett_debit_credit_bal_reporting=nett,
            used_for_calculation=calc,
            method_to_allocate_usd_purchase=meth,
        )
        mdl.save()
        # return redirect('index_view')
        return JsonResponse({
            'status': 1
        })
def grp_alter(request,pk):
    if request.method=='POST':
        grp =GrpAlter.objects.get(id=pk)
        grp.name = request.POST.get('name')
        grp.alias = request.POST.get('alias')
        grp.under = request.POST.get('under')
        grp.nature = request.POST.get('nature')
        grp.grp = request.POST.get('grp')
        grp.nett = request.POST.get('nett')
        grp.used = request.POST.get('used')
        grp.method = request.POST.get('method')
        
        
        grp.save()
        return redirect('group')
    return render(request, 'grp_alter.html',)


def grp(request,pk):
    grp=GrpAlter.objects.get(id=pk)
    return render(request, 'grp_alter.html',{'i':grp})

def group(request):
    grp=GrpAlter.objects.all()
    context={'grp':grp,}
    return render(request, 'groups.html',context)
