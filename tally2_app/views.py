from asyncio.windows_events import NULL
from django.shortcuts import render,redirect
from django.contrib import messages

from tally2_app.models import Companies, Create_attendence, Create_employeegroup, Currency_alt, Employee, Months, Rounding, Under, Voucher, compute_information, cost_centre, create_payhead, currencyAlteration, emp_category, gratuity, ledger_bankdetails, ledger_cheque_demension, salary, statistics_Accounts, statistics_Total_Voucher, statistics_Voucher_Register, statistics_Voucher_count, statistics_Vouchers, stock_itemcreation, stockgroupcreation, tally_group, tally_ledger, unit_compound, unit_simple


# Create your views here.
def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'Statistics.html')

def Statements_accounts(request):

        return render(request,'Statements_accounts.html')
   

def statistics(request):
    
    
    groups_count = tally_group.objects.all().count()
    centres_count= cost_centre.objects.all().count()
    ledgers_count = tally_ledger.objects.all().count()
    
    sgtotal=stockgroupcreation.objects.count()
    sitotal=stock_itemcreation.objects.count()
    vt_total=Voucher.objects.count()

    att1=Create_attendence.objects.count()
    uni1=unit_simple.objects.count()
    uni2=unit_compound.objects.count()
    uni3=uni1+uni2
    cur3=currencyAlteration.objects.count()
    empg=Create_employeegroup.objects.count()
    emp=Employee.objects.count()
    voucher =statistics_Vouchers.objects.all().order_by('Vouchers_name')
    accounts = statistics_Accounts.objects.all()
    sum=0
    total1= statistics_Total_Voucher.objects.all()
    for i in total1:
        if i.Total:
            sum+=i.Total

    
    context={
       'groups_count':groups_count,
       'centres_count':centres_count,
       'ledgers_count':ledgers_count,
        'vt_total':vt_total,
        'sgtotal':sgtotal,
        'sitotal':sitotal,
        'voucher':voucher,
        'sum':sum,
        'accounts':accounts,
        'att1':att1,
        'uni3':uni3,
        'cur3':cur3,
        'empg':empg,
        'emp':emp,
    }
    return render(request, 'Statistics.html',context)


  

def Statistics_list_of_ledger(request):
    groups_count1 = tally_group.objects.all().count()
    
  
    ledgers_count1 = tally_ledger.objects.all().count()
    
    grpp=Under.objects.all()
    context={
        'grpp':grpp,
        "groups_count1":groups_count1,
        "ledgers_count1" : ledgers_count1
    
    }
   
    return render(request,'Statistics_LedgersList.html',context)

# return redirect('/') '''

def Statistics_list_of_groups(request):
    grp=tally_group.objects.all()
    groups_count2 = tally_group.objects.all().count()
    

    context={
        
        'grp':grp,

        "groups_count2": groups_count2,
        
        }
     
    return render(request,'Statistics_GroupsList.html',context)

def Statistics_list_of_cost_centers(request):
   
    cst=cost_centre.objects.all()
    cost_centre_count=cost_centre.objects.all().count()
    context={
                    'cst':cst,
                    'cost_centre_count':cost_centre_count,
                   

        }
    return render(request,'Statistics_CostCentresList.html',context)
   
# def shut_card(request):
#     return render(request,'shut_card.html')
'''
def load_ledger_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.get(id=pk)
        lga=tally_group.objects.filter(id=t_id)
        if request.method=='POST':
            led.name=request.POST.get('name')
            led.alias=request.POST.get('alias')
            led.under=request.POST.get('under')
            led.mname=request.POST.get('mailingname')
            led.address=request.POST.get('address')
            led.state=request.POST.get('state')
            led.country=request.POST.get('country')
            led.pincode=request.POST.get('pincode')
            led.pan_no=request.POST.get('pan_no')
            led.bank_details=request.POST.get('bank_details')
            led.registration_type=request.POST.get('registration_type')
            led.gst_uin=request.POST.get('gst_uin')
            led.opening_blnc=request.POST.get('opening_blnc')

            led.set_odl=request.POST.get('set_odl')
            led.aac_holder_nm=request.POST.get('ac_holder_nm')
            led.acc_no=request.POST.get('acc_no')
            led.ifsc_code=request.POST.get('ifsc_code')
            led.swift_code=request.POST.get('swift_code')
            led.bank_name=request.POST.get('bank_name')
            led.branch=request.POST.get('branch')
            led.SA_cheque_bk=request.POST.get('SA_cheque_bk')
            led.Echeque_p=request.POST.get('Echeque_p')
            led.SA_chequeP_con=request.POST.get('SA_chequeP_con')
            led.company_id=t_id
            led.save()
            print("added")
            return redirect('/')
        return render(request,'load_ledger_alter.html',{'i':led,'lga':lga,'tally':tally})
    return redirect('/')

def ledger_gst_details(request):
    return render(request,'ledger_gst_details.html')

def ledger_chequebook(request):
    if request.method=='POST':
        cr=request.POST.get('ccon')
        fnum=request.POST.get('from_no')
        tnum=request.POST.get('to_no')
        nchq=request.POST.get('no_chq')
        nachq=request.POST.get('nm_chq')
        chqbk=ledger_chequebook(chq_range=cr,
                                from_num=fnum,
                                to_no=tnum,
                                no_chq=nchq,
                                nm_chq=nachq,
                
                                    )
        
        chqbk.save()
        print("added")
        return redirect('ledger_chequebook')
    return render(request,'ledger_cheque_book.html')

def ledger_bank_details(request):
    if request.method=='POST':
        bdt=request.POST['bankde']
        tt=request.POST['trans']
        cu=request.POST['cros']
        an=request.POST['acnt']
        ifs=request.POST['ifs']
        bn=request.POST['bank']
        bd=ledger_bankdetails(bank_de=bdt,
                        trans_type=tt,
                        cros_using=cu,
                        acnt_no=an,
                        ifs=ifs,
                        bank_name=bn,)
        
        bd.save()
        print("added")
    return render(request,'ledger_bank_details.html')


def load_cost_centers(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        cst=cost_centre.objects.get(id=pk)
        ccst=cost_centre.objects.filter(id=t_id)
        if request.method=='POST':
            cst.c_name=request.POST['cname']
            cst.cost_alias=request.POST['calias']
            cst.under=request.POST['cunder']
            cst.company_id=t_id
            cst.save()
            print("added")
            return redirect('/')
        return render(request,'load_cost_centers.html',{'i':cst,'ccst':ccst,'tally':tally})
    return redirect('/')

def alter_cost_create(request):
    ccst=cost_center.objects.all()
    if request.method=='POST':
        cname=request.POST['cname']
        calias=request.POST['calias']
        cunder=request.POST['cunder']
        cost=cost_center(c_name=cname,
                cost_alias=calias,
                under=cunder,
                )
        cost.save()
        print("added")
        return redirect('alter_cost_create')
    return render(request,'alter_cost_create.html',{'ccst':ccst})

def ledger_cheque_dimenssion(request):
    
    if request.method == 'POST':
            cc=request.POST.get('ccon')
            cw= request.POST.get('cheque_width')
            ch= request.POST.get('cheque_height')
            sle= request.POST.get('startL_leftEdge')
            slte= request.POST.get('startL_topEdge')
            dlle= request.POST.get('distancel_leftEdge')
            dlte= request.POST.get('distancel_topEdge')
            ds= request.POST.get('date_style')
            dts= request.POST.get('date_seperator')
            sw= request.POST.get('separator_width')
            cd= request.POST.get('character_distance')
            pdle= request.POST.get('Pdistancel_leftEdge')
            pdlte= request.POST.get('Pdistancel_topEdge')
            aw= request.POST.get('area_width')
            sldte= request.POST.get('secondL_DTE')
            sflh= request.POST.get('secondfirstL_height')
            fldte= request.POST.get('firstL_dTE')
            slfle= request.POST.get('sl_fisrtl_LE')
            slsle= request.POST.get('sl_secondl_LE')
            awa= request.POST.get('amount_widtharea')
            cfnmp= request.POST.get('currencyFNM_print')
            dfte= request.POST.get('df_TE')
            sle= request.POST.get('startL_LE')
            amwa= request.POST.get('amt_widtharea')
            csp= request.POST.get('currencyS_print')
            cn= request.POST.get('company_name')
            pcn= request.POST.get('print_CN')
            sfs= request.POST.get('salutation_Fsign')
            sss= request.POST.get('salutation_Ssign')
            tes= request.POST.get('top_Edistance')
            slfl= request.POST.get('startLF_leftE')
            wsa= request.POST.get('width_sign_area')
            hsa= request.POST.get('height_sign_area')

            cld= ledger_cheque_demension(cheque_config=cc,cheque_width=cw,cheque_height=ch,startL_leftEdge=sle,startL_topEdge=slte,distancel_leftEdge=dlle,
                                        distancel_topEdge=dlte,date_style=ds,date_seperator=dts,separator_width=sw,character_distance=cd,
                                        Pdistancel_leftEdge=pdle,Pdistancel_topEdge=pdlte,area_width=aw,secondL_DTE=sldte,secondfirstL_height=sflh,
                                        firstL_dTE=fldte,sl_fisrtl_LE=slfle,sl_secondl_LE=slsle,amount_widtharea=awa,currencyFNM_print=cfnmp,
                                        df_TE=dfte,startL_LE=sle,amt_widtharea=amwa,currencyS_print=csp,company_name=cn,print_CN=pcn,
                                        salutation_Fsign=sfs,salutation_Ssign=sss,top_Edistance=tes,startLF_leftE=slfl,width_sign_area=wsa,
                                        height_sign_area=hsa)

            cld.save()
            return redirect('ledger_cheque_dimenssion')
    return render(request,'ledger_cheque_dimenssion.html')
    '''

#-------------------------Anandha Krishnan --------------------------------
def Statistics_voucher_monthly_register(request,id):
    mo = Months.objects.all()

    vch = statistics_Vouchers.objects.get(id=id)
    count = statistics_Voucher_count.objects.filter(Voucher=id)
    total=0
    for i in count:
        if i.Total_Voucher:
            total+=i.Total_Voucher

    if statistics_Total_Voucher.objects.filter(Voucher=id):
        to=statistics_Total_Voucher.objects.get(Voucher=id)
        to.Voucher=vch
        to.Total=total
        to.save()
    else:
        to=statistics_Total_Voucher()
        to.Voucher=vch
        to.Total=total
        to.save()
   


    context = {
        'mo':mo,
        'vch':vch,
        'count':count,
        'total':total,
        
        
        
        

    }

    
    return render(request,'statistics_voucher_monthly_register.html',context)

def Statistics_voucher_register(request,id,pk):
    voucher = statistics_Voucher_Register.objects.filter(Month=id,Voucher=pk)
    vch = statistics_Vouchers.objects.get(id=pk)
    

    total_debit=0
    total_credit=0

    for i in voucher:
        if i.Debit_Amount:
            total_debit +=i.Debit_Amount
        if i.Credit_Amount:
            total_credit +=i.Credit_Amount


    v=statistics_Vouchers.objects.get(id=pk)
    m=Months.objects.get(id=id)
    count = voucher.count()
    if statistics_Voucher_count.objects.filter(Month=id,Voucher=pk):
        total= statistics_Voucher_count.objects.get(Month=id,Voucher=pk)
        
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()
    else:
        total= statistics_Voucher_count()
        total.Voucher=v
        total.Month=m
        total.Total_Voucher=count
        


        total.save()


    context = {
        'voucher':voucher,
        'total_debit':total_debit,
        'total_credit':total_credit,
        'vch':vch,
        'm':m,

    }

    
    return render(request,'statistics_voucher_register.html',context)




def Statistics_voucher_Delete(request,id,pk,de):
    voucher = statistics_Voucher_Register.objects.get(id=de)
    voucher.delete()
    

    return redirect(Statistics_voucher_register,id,pk)

#------------------------------------------Rehanas---------------------------------------------
#  units------

def statistics_units(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    sunits=unit_simple.objects.all()
    cunits=unit_compound.objects.all()
    uni1=unit_simple.objects.count()
    uni2=unit_compound.objects.count()
    uni3=uni1+uni2
    context={'sunits':sunits,'cunits':cunits,'uni3':uni3}
    return render(request,'st_units.html',context) 

def statistics_unit_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    uni=unit_simple.objects.filter(id=pk)
    context={'uni':uni}
    return render(request,'st_unit_alter.html',context)   

def statistics_su_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        sgrp =unit_simple.objects.get(id=pk)
        sgrp.symbol = request.POST.get('symbol')
        sgrp.formal_name = request.POST.get('formal_name')
        sgrp.decimal = request.POST.get('decimal')
        sgrp.uqc = request.POST.get('uqc')
        sgrp.save()
        return redirect('statistics_units')
    return render(request, 'st_units.html')     

def statistics_cunit_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    uni=unit_compound.objects.filter(id=pk)
    uuu=unit_simple.objects.all()
    context={'uni':uni,'uuu':uuu}
    return render(request,'st_unitalteration.html',context)     

def statistics_cu_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        cmp =unit_compound.objects.get(id=pk)
        cmp.f_unit = request.POST.get('first_unit')
        cmp.conversion = request.POST.get('conversion')
        cmp.s_unit = request.POST.get('second_unit')
        cmp.save()
        return redirect('statistics_units')
    return render(request, 'st_units.html')   



#  currencies-----           

def statistics_currencies(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    currencyd=currencyAlteration.objects.filter(id=1)
    currencydff=currencyAlteration.objects.all().exclude(id=1)
    currency=Currency_alt.objects.all()
    cur3=currencyAlteration.objects.count()
    context={'currencyd':currencyd,'cur3':cur3,'currency':currency,'currencydff':currencydff}
    return render(request,'st_currencies.html',context)  

def statistics_curr_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    curr=currencyAlteration.objects.filter(id=pk)
    context={'curr':curr}
    return render(request,'st_curr_alter.html',context)    

def statistics_cdef_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        cur =currencyAlteration.objects.get(id=pk)
        cur.Symbol = request.POST.get('c_symbl')
        cur.FormalName = request.POST.get('fname')
        cur.ISOCurrency = request.POST.get('isocode')
        cur.DecimalPlace = request.POST.get('decimal_p')
        cur.showAmount = request.POST.get('show_amt')
        cur.suffixSymbol = request.POST.get('suffix')
        cur.AddSpace = request.POST.get('add_space')
        cur.wordRep = request.POST.get('word_rep')
        cur.DecimalWords = request.POST.get('no_decimal')
        cur.save()
        return redirect('statistics_currencies')
    return render(request, 'st_currencies.html')       

def statistics_curr_alter2(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    curr=currencyAlteration.objects.filter(id=pk)
    curr1=Currency_alt.objects.filter(currencyAlteration_id=pk)
    context={'curr':curr,'curr1':curr1}
    return render(request,'st_currency_alter2.html',context)    



def statistics_curr_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        curr = currencyAlteration.objects.get(id=pk)
        curr.Symbol=request.POST.get('symbol')
        curr.FormalName=request.POST.get('name')
        curr.ISOCurrency=request.POST.get('iso')
        curr.DecimalPlace=request.POST.get('numdec')
        curr.showAmount=request.POST.get('amount')
        curr.suffixSymbol=request.POST.get('suffix')
        curr.AddSpace=request.POST.get('symam')
        curr.wordRep=request.POST.get('amodec')
        curr.DecimalWords=request.POST.get('decwo')

        curr.stddate=request.POST.get('standate')
        curr.stdrate=request.POST.get('stdrate')
        curr.selldate=request.POST.get('selldate')
        curr.selvorate=request.POST.get('selvrate')
        curr.sellrate=request.POST.get('selsrate')
        curr.buydate=request.POST.get('buydate')
        curr.buyvorate=request.POST.get('buyvrate')
        curr.buyrate=request.POST.get('buysrate')
         
        curr.save()                     
        return redirect('statistics_currencies')
    return render(request,'currencies.html')      

#  Attendence / Production types -----       

def statistics_atten_prod(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    attendance=Create_attendence.objects.all()
    att1=Create_attendence.objects.count()
    context={'att1':att1,'attendance':attendance}
    return render(request,'st_attend_prod.html',context)   

def statistics_atten_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    att=Create_attendence.objects.filter(id=pk)
    attendance=Create_attendence.objects.all()
    context={'att':att,'attendance':attendance}
    return render(request,'st_attendance_alter.html',context)    

def statistics_atten_alter(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        attend =Create_attendence.objects.get(id=pk)
        attend.name = request.POST.get('name')
        attend.alias = request.POST.get('alias')
        attend.under = request.POST.get('under_name')
        attend.type = request.POST.get('attendance')
        attend.period = request.POST.get('period')
        attend.units = request.POST.get('units')
        attend.save()
        return redirect('statistics_atten_prod')
    return render(request, 'st_attend_prod.html')    

def statistics_att_create(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    aaa = Create_attendence.objects.all()
    context = {'aaa':aaa}
    return render(request,'st_attend_create.html',context)    

def statistics_add_attend(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        under_name = request.POST.get('show_amt')
        attendance = request.POST.get('attendance')
        period = request.POST.get('period')
        atten = Create_attendence(name=name,
                                   alias=alias,
                                   under=under_name,
                                   type=attendance,
                                   period=period)
        atten.save()
        return redirect('statistics_atten_prod')
    return render(request, 'st_attend_prod.html')


#  Employee Groups---------

def statistics_emp_groups(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    p_cost=emp_category.objects.all()
    empg=Create_employeegroup.objects.all()
    cost=emp_category.objects.count()
    empg1=Create_employeegroup.objects.count()
    context={'p_cost':p_cost,'empg':empg,'empg1':empg1,'cost':cost}
    return render(request,'st_employee_group.html',context)  

  
def statistics_p_cost(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    pcos=emp_category.objects.filter(id=pk)
    context={'pcos':pcos}
    return render(request,'st_pcost_alter.html',context)  

def statistics_pcost_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        pcost =emp_category.objects.get(id=pk)
        pcost.cat_name = request.POST.get('name')
        pcost.cat_alias = request.POST.get('alias')
        pcost.revenue_items = request.POST.get('revenue')
        pcost.non_revenue_items = request.POST.get('non_revenue')
        pcost.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')      
     

def statistics_eg_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    empalter=Create_employeegroup.objects.filter(id=pk)
    emp=Create_employeegroup.objects.all()
    context={'empalter':empalter,'emp':emp}
    return render(request,'st_emp_group_alter.html',context)    

def statistics_empgrp_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        empga =Create_employeegroup.objects.get(id=pk)
        empga.name = request.POST.get('name')
        empga.alias = request.POST.get('alias')
        empga.under_name = request.POST.get('under_name')
        empga.salary_details = request.POST.get('salary')
        empga.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')      

def statistics_empg_dtls(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    empgd=Create_employeegroup.objects.filter(id=pk)
    epay=create_payhead.objects.all()
    if request.method=='POST':
        name1=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=salary(name=name1,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   pay_type=payhead,
                   cal_type=calculation,
        )
        std.save()
        return redirect('statistics_emp_groups')
    return render(request,'st_empg_details.html',{'epay':epay,'empgd':empgd}) 


def statistics_create_payhd(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    ph=Create_attendence.objects.filter(type="Attendance/Leave with pay")
    ph2=Create_attendence.objects.filter(type="Production")
    std=Create_attendence.objects.all()
    return render(request,'st_pay_head.html',{'std':std,'ph':ph,'ph2':ph2}) 


def statistics_add_payhead(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        return redirect('/')
    return render(request,'st_pay_head.html')  

def statistics_add_salaryd(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        empga =Create_employeegroup.objects.get(id=pk)
        empga.name = request.POST.get('name')
        empga.alias = request.POST.get('alias')
        empga.under_name = request.POST.get('under_name')
        empga.salary_details = request.POST.get('salary')
        empga.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')   


def statistics_empg_create(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    aaa = Create_employeegroup.objects.all()
    context = {'aaa':aaa}
    return render(request,'st_create_empg.html',context)     

def statistics_add_empg(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        name = request.POST.get('name')
        alias = request.POST.get('alias')
        under_name = request.POST.get('show_amt')
        salary_details = request.POST.get('salary')
        atten = Create_attendence(name=name,
                                   alias=alias,
                                   under=under_name,
                                   type=salary_details)
        atten.save()
        return redirect('statistics_emp_groups')
    return render(request, 'st_employee_group.html')    



# Employee -------


def statistics_employee(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    p_cost=emp_category.objects.all()
    empg=Create_employeegroup.objects.all()
    emp=Employee.objects.all()
    cost=emp_category.objects.count()
    empg1=Create_employeegroup.objects.count()
    empg2=Employee.objects.count()
    context={'p_cost':p_cost,'empg':empg,'emp':emp,'cost':cost,'empg1':empg1,'empg2':empg2}
    return render(request,'st_employee.html',context)

    
def statistics_emp_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    emm=Employee.objects.filter(id=pk)
    empg=Create_employeegroup.objects.all()
    context={'emm':emm,'empg':empg}
    return render(request,'st_employee_alter.html',context)  

  
def statistics_employee_alt(request,pk):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        empp =Employee.objects.get(id=pk)
        empp.name =request.POST.get('name')
        empp.alias=request.POST.get('alias')
        empp.under=request.POST.get('under')
        empp.defn_sal=request.POST.get('sal')
        empp.emp_name=request.POST.get('empname')
        empp.emp_desg=request.POST.get('desig')
        empp.fnctn=request.POST.get('fn')
            

        empp.location=request.POST.get('loc')
        empp.gender=request.POST.get('gen')
        empp.blood=request.POST.get('blood')
        empp.parent_name=request.POST.get('prnts')
        empp.spouse_name=request.POST.get('spouse')
        empp.address=request.POST.get('adrs')
        empp.number=request.POST.get('phone')

        empp.email=request.POST.get('email')
        empp.bankdtls=request.POST.get('bank')
        empp.inc_tax_no=request.POST.get('incno')
        empp.aadhar_no=request.POST.get('adhar')
        empp.uan=request.POST.get('uan')
        empp.pfn=request.POST.get('pf')
        empp.pran=request.POST.get('pr')
        empp.esin=request.POST.get('esi')

 
            
        empp.save()
        return redirect('statistics_employee')
    return render(request,'st_employee.html')  

    #----------------------------------------Mohammed Arif --------------------------------------------
    # stkgrp ---------------

def Statistics_Stock_Groups(request):
    sgdata=stockgroupcreation.objects.all()
    # SGdata=stock_itemcreation.objects.all()
    sqtotal=stockgroupcreation.objects.count()
    # swtotal=stock_itemcreation.objects.count()
    context={'sgdata':sgdata,'sqtotal':sqtotal}
    return render(request,'stockgroup.html',context)

def Statistics_Stock_Group_Creation_Page(request):
    sg_data=stockgroupcreation.objects.all()
    context={'sg_data':sg_data}
    return render(request,'stockgrpcreationpage.html',context)

def Statistics_Stock_Group_Creation(request):
    if request.method =='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']

        data=stockgroupcreation(name=name,alias=alias,under=under_name,quantities=quantities)
        data.save()
        return redirect("Statistics_Stock_Groups")

def Statistics_Stock_Group_Edit_Page(request,pk):
    sg_data=stockgroupcreation.objects.all()
    sgedit=stockgroupcreation.objects.get(id=pk)
    context={'sgedit':sgedit,'sg_data':sg_data}
    return render(request,"editstockgroup.html",context)

def Statistics_Edit_Stock_Group(request,pk):
    if request.method =='POST':
        sgdata=stockgroupcreation.objects.get(id=pk)
        sgdata.name=request.POST['name']
        sgdata.alias=request.POST['alias']
        sgdata.under=request.POST['under_name']
        sgdata.quantities=request.POST['quantities']

        sgdata.save()
        return redirect('Statistics_Stock_Groups')
    return render(request,'editstockgroup.html')

def Statistics_Delete_Stock_Group(request,pk):
    stk=stockgroupcreation.objects.get(id=pk)
    stk.delete()
    return redirect('Statistics_Stock_Groups')

# syk item--------------------

def Statistics_Stock_Items(request):
    sgdata=stockgroupcreation.objects.all()
    sidata=stock_itemcreation.objects.all()
    sgtotal=stockgroupcreation.objects.count()
    sitotal=stock_itemcreation.objects.count()
    context={'sgdata':sgdata,'sgtotal':sgtotal,'sidata':sidata,'sitotal':sitotal}
    return render(request,'stockitem.html',context)

def Statistics_Stock_Item_Creation_Page(request):
    si_data=stock_itemcreation.objects.all()
    grp=stockgroupcreation.objects.all()
    unt=unit_compound.objects.all()
    u=unit_simple.objects.all()
    context={'si_data':si_data,"grp":grp,'u':u,'unt':unt}
    return render(request,'stockitemcreationpage.html',context)


def Statistics_Stock_Item_Creation(request):
    if request.method=='POST':
        nm=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        units=request.POST['units']
        gst_applicable=request.POST['gst_applicable']
        set_alter=request.POST['set_alter']
        typ_sply=request.POST['typ_sply']
        rate_of_duty=request.POST['rate_of_duty']
        
        crt=stock_itemcreation(name=nm,alias=alias,under=under,units=units,typ_sply=typ_sply,
        gst_applicable=gst_applicable,set_alter=set_alter,rate_of_duty=rate_of_duty)
        crt.save()
        
        return redirect('Statistics_Stock_Items')



def Statistics_Stock_Item_Edit_Page(request,pk):
    si_data=stock_itemcreation.objects.all()
    grp=stockgroupcreation.objects.all()
    unt=unit_compound.objects.all()
    u=unit_simple.objects.all()
    sidata=stock_itemcreation.objects.get(id=pk)
    context={'edit':sidata,"si_data":si_data,'grp':grp,'unt':unt,'u':u}
    return render(request,"editstockitem.html",context)

def Statistics_Edit_Stock_Item(request,pk):
    if request.method =='POST':
        sidata=stock_itemcreation.objects.get(id=pk)
        sidata.name=request.POST['name']
        sidata.alias=request.POST['alias']
        sidata.under=request.POST['under']
        sidata.units=request.POST['units']
        sidata.gst_applicable=request.POST['gst_applicable']
        sidata.set_alter=request.POST['set_alter']
        sidata.typ_sply=request.POST['typ_sply']
        sidata.rate_of_duty=request.POST['si_data']
        sidata.quantity=request.POST['quantity']
        sidata.rate=request.POST['rate']
        sidata.per=request.POST['per']
        sidata.value=request.POST['value']

        sidata.save()
        return redirect('Statistics_Stock_Items')
    return render(request,'editstockitem.html')

def Statistics_Delete_Stock_Item(request,pk):
    stk=stock_itemcreation.objects.get(id=pk)
    stk.delete()
    return redirect('Statistics_Stock_Items')

# vchr typ ---------------------

def Statistics_Voucher_Types(request):
    vt_data=Voucher.objects.all()
    vt_total=Voucher.objects.count()
    context={'vt_data':vt_data,'vt_total':vt_total}
    return render(request,'vouchertype.html',context)

def Statistics_Voucher_Type_Creation_Page(request):
    data=Voucher.objects.all()
    context={'data':data}
    return render(request,'vouchertypecreationpage.html',context)

def Statistics_Voucher_Type_Creation(request):
        if request.method=='POST':
            nm=request.POST['vname']
            als=request.POST['alias']
            vtp=request.POST['vouch_type']
            abbr=request.POST['Abbreviation']
            actp=request.POST['activate_Vtype']
            mvno=request.POST['method_Vno']
            prnt=request.POST['prevent']
            acn=request.POST['advance_con']
            use=request.POST['use_EDV']
            zero=request.POST['zero_val']
            mvd=request.POST['mVoptional_defualt']
            anar=request.POST['allow_nar']
            prvdl=request.POST['provide_L']
            jrnl=request.POST['manu_jrnl']
            track=request.POST['track_purchase']
            enbl=request.POST['enable_acc']
            prntva=request.POST['prnt_VA_save']
            prntfml=request.POST['prnt_frml']
            juri=request.POST['jurisdiction']
            tprint=request.POST['title_print']
            setaltr=request.POST['set_alter']
            posinv=request.POST['pos_invoice']
            msg1=request.POST['msg_1']
            msg2=request.POST['msg_2']
            dbank=request.POST['default_bank']
            nc=request.POST['name_class']

            vhr=Voucher(voucher_name=nm,
                        alias = als,
                        voucher_type = vtp,
                        abbreviation = abbr,
                        voucherActivate = actp,
                        voucherNumber = mvno,
                        preventDuplicate = prnt,
                        advance_con = acn,
                        voucherEffective = use,
                        transaction = zero,
                        make_optional = mvd,
                        voucherNarration = anar,
                        provideNarration = prvdl,
                        manu_jrnl = jrnl,
                        track_purchase = track,
                        enable_acc = enbl,
                        prnt_VA_save = prntva,
                        prnt_frml = prntfml,
                        jurisdiction = juri,
                        title_print = tprint,
                        set_alter = setaltr,
                        pos_invoice = posinv,
                        msg_1 = msg1,
                        msg_2 = msg2,
                        default_bank = dbank,
                        name_class = nc,)          
            vhr.save()
            return redirect('Statistics_Voucher_Types')

def Statistics_Voucher_Type_Edit_Page(request,pk):
    vt_edit=Voucher.objects.get(id=pk)
    edit=Voucher.objects.all()
    context={'vt_edit':vt_edit,'edit':edit}
    return render(request,'vouchertypeeditpage.html',context)

def Statistics_Edit_Voucher_Types(request,pk):
    if request.method =='POST':
        vchrdata=Voucher.objects.get(id=pk)
        vchrdata.voucher_name=request.POST['vname']
        vchrdata.alias=request.POST['alias']
        # vchrdata.voucher_type=request.POST['vouch_type']
        vchrdata.abbreviation=request.POST['Abbreviation']
        vchrdata.voucherActivate=request.POST['activate_Vtype']
        vchrdata.voucherNumber=request.POST['method_Vno']
        vchrdata.preventDuplicate=request.POST['prevent']
        vchrdata.advance_con=request.POST['advance_con']
        vchrdata.voucherEffective=request.POST['use_EDV']
        vchrdata.transaction=request.POST['zero_val']
        vchrdata.make_optional=request.POST['mVoptional_defualt']
        vchrdata.voucherNarration=request.POST['allow_nar']
        vchrdata.provideNarration=request.POST['provide_L']
        vchrdata.manu_jrnl=request.POST['manu_jrnl']
        vchrdata.track_purchase=request.POST['track_purchase']
        vchrdata.enable_acc=request.POST['enable_acc']
        vchrdata.prnt_VA_save=request.POST['prnt_VA_save']
        vchrdata.prnt_frml=request.POST['prnt_frml']
        vchrdata.jurisdiction=request.POST['jurisdiction']
        vchrdata.title_print=request.POST['title_print']
        vchrdata.set_alter=request.POST['set_alter']
        vchrdata.pos_invoice=request.POST['pos_invoice']
        vchrdata.msg_1=request.POST['msg_1']
        vchrdata.msg_2=request.POST['msg_2']
        vchrdata.default_bank=request.POST['default_bank']
        vchrdata.name_class=request.POST['name_class']

    vchrdata.save()
    return redirect('Statistics_Voucher_Types')

def Statistics_Delete_Voucher_Type(request,pk):
    vt=Voucher.objects.get(id=pk)
    vt.delete()
    return redirect('Statistics_Voucher_Types')

