# Generated by Django 4.0.6 on 2022-09-17 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tally2_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('type', models.CharField(max_length=225)),
                ('period', models.CharField(blank=True, default='null', max_length=225)),
                ('units', models.CharField(blank=True, default='null', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Create_employeegroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('define_salary', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='create_payhead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('pay_type', models.CharField(max_length=225)),
                ('income_type', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('affect_net', models.CharField(max_length=225)),
                ('payslip', models.CharField(max_length=225)),
                ('calculation_of_gratuity', models.CharField(max_length=225)),
                ('cal_type', models.CharField(max_length=225)),
                ('calculation_period', models.CharField(max_length=225)),
                ('leave_withpay', models.CharField(max_length=225)),
                ('leave_with_out_pay', models.CharField(max_length=225)),
                ('production_type', models.CharField(max_length=225)),
                ('opening_balance', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='currencyAlteration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Symbol', models.CharField(max_length=255)),
                ('FormalName', models.CharField(max_length=255)),
                ('ISOCurrency', models.CharField(max_length=30, null=True)),
                ('DecimalPlace', models.IntegerField()),
                ('showAmount', models.CharField(max_length=20)),
                ('suffixSymbol', models.CharField(max_length=20)),
                ('AddSpace', models.CharField(max_length=20)),
                ('wordRep', models.CharField(max_length=255, null=True)),
                ('DecimalWords', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='emp_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=225)),
                ('cat_alias', models.CharField(max_length=225)),
                ('revenue_items', models.CharField(max_length=225)),
                ('non_revenue_items', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('date_join', models.DateField()),
                ('defn_sal', models.CharField(max_length=225)),
                ('emp_name', models.CharField(max_length=225)),
                ('emp_desg', models.CharField(max_length=225)),
                ('fnctn', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=225)),
                ('gender', models.CharField(max_length=225)),
                ('dob', models.DateField()),
                ('blood', models.CharField(max_length=225)),
                ('parent_name', models.CharField(max_length=225)),
                ('spouse_name', models.CharField(max_length=225)),
                ('address', models.CharField(max_length=225)),
                ('number', models.CharField(max_length=225)),
                ('email', models.CharField(max_length=225)),
                ('inc_tax_no', models.CharField(max_length=225)),
                ('aadhar_no', models.CharField(max_length=225)),
                ('uan', models.CharField(max_length=225)),
                ('pfn', models.CharField(max_length=225)),
                ('pran', models.CharField(max_length=225)),
                ('esin', models.CharField(max_length=225)),
                ('bankdtls', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('under', models.CharField(max_length=225)),
                ('effective', models.CharField(max_length=225)),
                ('payhead', models.CharField(max_length=225)),
                ('rate', models.CharField(max_length=225)),
                ('per', models.CharField(max_length=225)),
                ('pay_type', models.CharField(max_length=225)),
                ('cal_type', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='unit_compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=100)),
                ('f_unit', models.CharField(max_length=100, null=True)),
                ('conversion', models.IntegerField()),
                ('s_unit', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='unit_simple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=100)),
                ('formal_name', models.CharField(max_length=100)),
                ('uqc', models.CharField(max_length=100)),
                ('decimal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='uqcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uqc_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rounding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rounding_Method', models.CharField(blank=True, default='Null', max_length=225)),
                ('Round_limit', models.CharField(blank=True, default='Null', max_length=22)),
                ('pay_head_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.create_payhead')),
            ],
        ),
        migrations.CreateModel(
            name='gratuity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_of_months', models.CharField(max_length=225)),
                ('number_of_months_from', models.CharField(max_length=225)),
                ('to', models.CharField(max_length=225)),
                ('calculation_per_year', models.CharField(max_length=225)),
                ('pay_head_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.create_payhead')),
            ],
        ),
        migrations.CreateModel(
            name='E_found_trasfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acount_No', models.CharField(max_length=225)),
                ('IFSC_code', models.CharField(max_length=225)),
                ('Bank_name', models.CharField(max_length=225)),
                ('Cheque', models.CharField(max_length=225)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Currency_alt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stddate', models.CharField(blank=True, max_length=255, null=True)),
                ('stdrate', models.CharField(default='null', max_length=255)),
                ('selldate', models.CharField(blank=True, max_length=255, null=True)),
                ('selvorate', models.CharField(default='null', max_length=255)),
                ('sellrate', models.CharField(default='null', max_length=255)),
                ('buydate', models.CharField(blank=True, max_length=255, null=True)),
                ('buyvorate', models.CharField(default='null', max_length=255)),
                ('buyrate', models.CharField(default='null', max_length=255)),
                ('currencyAlteration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.currencyalteration')),
            ],
        ),
        migrations.CreateModel(
            name='compute_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compute', models.CharField(default='Null', max_length=225)),
                ('effective_from', models.CharField(default='NULL', max_length=225)),
                ('amount_greater', models.CharField(default='NULL', max_length=225)),
                ('amount_upto', models.CharField(default='NULL', max_length=225)),
                ('slab_type', models.CharField(default='NULL', max_length=225)),
                ('value', models.CharField(default='NULL', max_length=225)),
                ('Pay_head_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.create_payhead')),
            ],
        ),
        migrations.CreateModel(
            name='add_bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Acount_No', models.CharField(max_length=225)),
                ('IFSC_code', models.CharField(max_length=225)),
                ('Bank_name', models.CharField(max_length=225)),
                ('Branch_name', models.CharField(max_length=225)),
                ('Transaction_type', models.CharField(max_length=225)),
                ('employee_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.employee')),
            ],
        ),
    ]
