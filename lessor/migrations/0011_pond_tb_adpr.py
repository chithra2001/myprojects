# Generated by Django 4.2.1 on 2023-06-30 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessor', '0010_pond_tb_paccept_pond_tb_ppayment_pond_tb_preject'),
    ]

    operations = [
        migrations.AddField(
            model_name='pond_tb',
            name='Adpr',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
