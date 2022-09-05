# Generated by Django 4.0.6 on 2022-09-05 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tally2_app', '0005_companies_groupmodel_grpalter_grunder_tally_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='cost_centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=255)),
                ('cost_alias', models.CharField(max_length=255)),
                ('under', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.companies')),
            ],
        ),
        migrations.CreateModel(
            name='cost_center',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('cost_alias', models.CharField(max_length=255)),
                ('under', models.CharField(max_length=255)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tally2_app.companies')),
            ],
        ),
    ]
