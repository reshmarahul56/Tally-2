# Generated by Django 4.0.6 on 2022-09-05 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tally2_app', '0006_cost_centre_cost_center'),
    ]

    operations = [
        migrations.CreateModel(
            name='lbank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(blank=True, default='Null', max_length=100)),
                ('cross_using', models.CharField(blank=True, default='Null', max_length=200)),
                ('acno', models.CharField(blank=True, default='Null', max_length=100)),
                ('ifscode', models.CharField(blank=True, default='Null', max_length=200)),
                ('bankname', models.CharField(blank=True, default='Null', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='lcheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_no', models.CharField(max_length=100)),
                ('to_no', models.CharField(max_length=100)),
                ('no_cheques', models.CharField(max_length=100)),
                ('name_cheque', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ledger_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_alias', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_opening_bal', models.CharField(blank=True, default='Null', max_length=225)),
                ('ledger_type', models.CharField(blank=True, default='Null', max_length=225)),
                ('tax_gst_uin', models.CharField(blank=True, default='Null', max_length=225)),
                ('tax_register_type', models.CharField(blank=True, default='Null', max_length=225)),
                ('tax_pan_no', models.CharField(blank=True, default='Null', max_length=225)),
                ('tax_alter_gst_details', models.CharField(blank=True, default='Null', max_length=225)),
                ('sta_assessable_calculation', models.CharField(blank=True, default='Null', max_length=225)),
                ('sta_Appropriate_to', models.CharField(blank=True, default='Null', max_length=225)),
                ('sta_gst_applicable', models.CharField(blank=True, default='Null', max_length=225)),
                ('sta_Set_alter_GST', models.CharField(blank=True, default='Null', max_length=225)),
                ('sta_type_of_supply', models.CharField(blank=True, default='Null', max_length=225)),
                ('sta_Method_of_calc', models.CharField(blank=True, default='Null', max_length=225)),
                ('rou_Rounding_Method', models.CharField(blank=True, default='Null', max_length=225)),
                ('rou_Round_limit', models.CharField(blank=True, default='Null', max_length=22)),
                ('ta_type_of_duty_or_tax', models.CharField(blank=True, default='Null', max_length=225)),
                ('ta_type_of_tax', models.CharField(blank=True, default='Null', max_length=225)),
                ('ta_valuation_type', models.CharField(blank=True, default='Null', max_length=225)),
                ('ta_rate_per_unit', models.CharField(blank=True, default='Null', max_length=225)),
                ('ta_Persentage_of_calculation', models.CharField(blank=True, default='Null', max_length=225)),
                ('sun_maintain_balance_bill_by_bill', models.CharField(blank=True, default='Null', max_length=225)),
                ('sun_Default_credit_period', models.CharField(blank=True, default='Null', max_length=225)),
                ('sun_Check_for_credit_days', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_od_limit', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_holder_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_ac_number', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_ifsc', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_swift_code', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_bank_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_branch_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_alter_chk_bks', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_enbl_chk_printing', models.CharField(blank=True, default='Null', max_length=225)),
                ('bank_auto_recoun', models.CharField(blank=True, default='Null', max_length=225)),
                ('mail_name', models.CharField(blank=True, default='Null', max_length=225)),
                ('mail_address', models.CharField(blank=True, default='Null', max_length=225)),
                ('mail_state', models.CharField(blank=True, default='Null', max_length=225)),
                ('mail_country', models.CharField(blank=True, default='Null', max_length=225)),
                ('mail_pincode', models.CharField(blank=True, default='Null', max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='MainGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(blank=True, max_length=225)),
                ('under_group', models.CharField(max_length=225)),
                ('affect_gp', models.CharField(blank=True, max_length=255)),
                ('group', models.CharField(max_length=225)),
                ('nett_balance', models.CharField(max_length=225)),
                ('used_for', models.CharField(max_length=225)),
                ('method', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Print_Cheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('payee_name', models.CharField(max_length=100)),
                ('cheque_number', models.CharField(max_length=100)),
                ('cheque_date', models.CharField(max_length=100)),
                ('amt_words', models.CharField(max_length=100)),
                ('amt_number', models.CharField(max_length=100)),
                ('ledger_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tally2_app.ledger')),
            ],
        ),
        migrations.CreateModel(
            name='SubGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('alias', models.CharField(blank=True, max_length=225)),
                ('group', models.CharField(max_length=225)),
                ('nett_balance', models.CharField(max_length=225)),
                ('used_for', models.CharField(max_length=225)),
                ('method', models.CharField(max_length=225)),
                ('maingroup', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.maingroup')),
            ],
        ),
        migrations.CreateModel(
            name='Under',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='cost_center',
            name='company',
        ),
        migrations.RemoveField(
            model_name='cost_centre',
            name='company',
        ),
        migrations.DeleteModel(
            name='Costcentr',
        ),
        migrations.DeleteModel(
            name='GroupModel',
        ),
        migrations.DeleteModel(
            name='GrpAlter',
        ),
        migrations.DeleteModel(
            name='grunder',
        ),
        migrations.RemoveField(
            model_name='tally_group',
            name='company',
        ),
        migrations.DeleteModel(
            name='Companies',
        ),
        migrations.DeleteModel(
            name='cost_center',
        ),
        migrations.DeleteModel(
            name='cost_centre',
        ),
        migrations.DeleteModel(
            name='tally_group',
        ),
        migrations.AddField(
            model_name='maingroup',
            name='under',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.under'),
        ),
        migrations.AddField(
            model_name='ledger',
            name='subgroup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.subgroup'),
        ),
        migrations.AddField(
            model_name='lcheque',
            name='ledger_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tally2_app.ledger'),
        ),
        migrations.AddField(
            model_name='lbank',
            name='ledger_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tally2_app.ledger'),
        ),
    ]