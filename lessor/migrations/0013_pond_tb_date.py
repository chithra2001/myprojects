# Generated by Django 4.2.1 on 2023-06-30 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lessor', '0012_rename_paccept_pond_tb_pstatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pond_tb',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
