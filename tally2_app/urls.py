from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
                #---------------------------------Reshma---------------------------------------------
                path('Statements_accounts',views.Statements_accounts,name='Statements_accounts'),
                path('',views.statistics,name='statistics'),
                path('base',views.base,name='base'),
                path('index',views.index,name='index'), 
                path('Statistics_list_of_groups',views.Statistics_list_of_groups,name='Statistics_list_of_groups'),
                path('Statistics_list_of_cost_centers',views.Statistics_list_of_cost_centers,name='Statistics_list_of_cost_centers'),
                path('Statistics_list_of_ledger',views.Statistics_list_of_ledger,name='Statistics_list_of_ledger'),

                #--------------------------------Anandha Krishnan -----------------------------------

                path('Statistics_voucher_monthly_register/<int:id>',views.Statistics_voucher_monthly_register,name='Statistics_voucher_monthly_register'),

                path('Statistics_voucher_register/<int:id>/<int:pk>',views.Statistics_voucher_register,name='Statistics_voucher_register'),

                    
                path('Statistics_voucher_Delete/<int:id>/<int:pk>/<int:de>',views.Statistics_voucher_Delete,name='Statistics_voucher_Delete'),

                #----------------------------------Rehanas------------------------------------------------

                path('statistics_units/',views.statistics_units,name='statistics_units'),
                path('statistics_unit_alter/<int:pk>',views.statistics_unit_alter,name='statistics_unit_alter'),
                path('statistics_cunit_alter/<int:pk>',views.statistics_cunit_alter,name='statistics_cunit_alter'),
                path('statistics_su_alter/<int:pk>',views.statistics_su_alter,name='statistics_su_alter'),
                path('statistics_cu_alter/<int:pk>',views.statistics_cu_alter,name='statistics_cu_alter'),

                path('statistics_currencies/',views.statistics_currencies,name='statistics_currencies'),
                path('statistics_curr_alter/<int:pk>',views.statistics_curr_alter,name='statistics_curr_alter'),   
                path('statistics_curr_alter2/<int:pk>',views.statistics_curr_alter2,name='statistics_curr_alter2'),
                path('statistics_cdef_alt/<int:pk>',views.statistics_cdef_alt,name='statistics_cdef_alt'),
                path('statistics_curr_alt/<int:pk>',views.statistics_curr_alt,name='statistics_curr_alt'),

                path('statistics_atten_prod/',views.statistics_atten_prod,name='statistics_atten_prod'),
                path('statistics_atten_alt/<int:pk>',views.statistics_atten_alt,name='statistics_atten_alt'),
                path('statistics_atten_alter/<int:pk>',views.statistics_atten_alter,name='statistics_atten_alter'),
                path('statistics_att_create/',views.statistics_att_create,name='statistics_att_create'),
                path('statistics_add_attend/',views.statistics_add_attend,name='statistics_add_attend'),

                path('statistics_emp_groups/',views.statistics_emp_groups,name='statistics_emp_groups'),
                path('statistics_p_cost/<int:pk>',views.statistics_p_cost,name='statistics_p_cost'),
                path('statistics_eg_alt/<int:pk>',views.statistics_eg_alt,name='statistics_eg_alt'),
                path('statistics_pcost_alt/<int:pk>',views.statistics_pcost_alt,name='statistics_pcost_alt'),
                path('statistics_empgrp_alt/<int:pk>',views.statistics_empgrp_alt,name='statistics_empgrp_alt'),
                path('statistics_empg_dtls/<int:pk>',views.statistics_empg_dtls,name='statistics_empg_dtls'),
                path('statistics_create_payhd/',views.statistics_create_payhd,name='statistics_create_payhd'),
                path('statistics_empg_create/',views.statistics_empg_create,name='statistics_empg_create'),
                path('statistics_add_empg/',views.statistics_add_empg,name='statistics_add_empg'),

                path('statistics_employee/',views.statistics_employee,name='statistics_employee'),
                path('statistics_emp_alt/<int:pk>',views.statistics_emp_alt,name='statistics_emp_alt'),
                path('statistics_employee_alt/<int:pk>',views.statistics_employee_alt,name='statistics_employee_alt'),

                path('statistics_add_payhead/',views.statistics_add_payhead,name='statistics_add_payhead'),

                #--------------------------------------Mohammed Arif---------------------------------------
                path('Statistics_Stock_Groups',views.Statistics_Stock_Groups,name="Statistics_Stock_Groups"),
                path('Statistics_Stock_Group_Creation_Page',views.Statistics_Stock_Group_Creation_Page,name="Statistics_Stock_Group_Creation_Page"),
                path('Statistics_Stock_Group_Creation',views.Statistics_Stock_Group_Creation,name='Statistics_Stock_Group_Creation'),
                path('Statistics_Stock_Group_Edit_Page/<int:pk>',views.Statistics_Stock_Group_Edit_Page,name='Statistics_Stock_Group_Edit_Page'),
                path('Statistics_Edit_Stock_Group/<int:pk>',views.Statistics_Edit_Stock_Group,name='Statistics_Edit_Stock_Group'),
                path('Statistics_Delete_Stock_Group/<int:pk>',views.Statistics_Delete_Stock_Group,name='Statistics_Delete_Stock_Group'),

                path('Statistics_Stock_Items',views.Statistics_Stock_Items,name="Statistics_Stock_Items"),
                path('Statistics_Stock_Item_Creation_Page',views.Statistics_Stock_Item_Creation_Page,name="Statistics_Stock_Item_Creation_Page"),
                path('Statistics_Stock_Item_Creation',views.Statistics_Stock_Item_Creation,name='Statistics_Stock_Item_Creation'),
                path('Statistics_Stock_Item_Edit_Page/<int:pk>',views.Statistics_Stock_Item_Edit_Page,name='Statistics_Stock_Item_Edit_Page'),
                path('Statistics_Edit_Stock_Item/<int:pk>',views.Statistics_Edit_Stock_Item,name='Statistics_Edit_Stock_Item'),
                path('Statistics_Delete_Stock_Item/<int:pk>',views.Statistics_Delete_Stock_Item,name='Statistics_Delete_Stock_Item'),

                path('Statistics_Voucher_Types',views.Statistics_Voucher_Types,name="Statistics_Voucher_Types"),
                path('Statistics_Voucher_Type_Creation_Page',views.Statistics_Voucher_Type_Creation_Page,name='Statistics_Voucher_Type_Creation_Page'),
                path('Statistics_Voucher_Type_Creation',views.Statistics_Voucher_Type_Creation,name='Statistics_Voucher_Type_Creation'),
                path('Statistics_Voucher_Type_Edit_Page/<int:pk>',views.Statistics_Voucher_Type_Edit_Page,name='Statistics_Voucher_Type_Edit_Page'),
                path('Statistics_Edit_Voucher_Types/<int:pk>',views.Statistics_Edit_Voucher_Types,name='Statistics_Edit_Voucher_Types'),
                path('Statistics_Delete_Voucher_Type/<int:pk>',views.Statistics_Delete_Voucher_Type,name='Statistics_Delete_Voucher_Type'),

            ]
''' path('list_of_groups',views.list_of_groups,name='list_of_groups'),
                path('load_create_groups/<int:pk>',views.load_create_groups,name='load_create_groups'),

                path('load_alter_groups',views.load_alter_groups,name="load_alter_groups"),
    # path('branch',views.branch,name='branch'),
    # path('ledger',views.ledger,name='ledger'),
                path('list_of_ledger',views.list_of_ledger,name='list_of_ledger'),
                path('load_ledger_alter/<int:pk>',views.load_ledger_alter,name='load_ledger_alter'),
                path('ledger_gst_details',views.ledger_gst_details,name='ledger_gst_details'),
                path('load_create_ledger',views.load_create_ledger,name='load_create_ledger'),
                path('ledger_chequebook',views.ledger_chequebook,name='ledger_chequebook'),
                path('ledger_bank_details',views.ledger_bank_details,name='ledger_bank_details'),
                path('ledger_cheque_dimenssion',views.ledger_cheque_dimenssion,name='ledger_cheque_dimenssion'),
'''
