# Generated by Django 4.2.1 on 2023-06-30 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessor', '0011_pond_tb_adpr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pond_tb',
            old_name='paccept',
            new_name='pstatus',
        ),
        migrations.RemoveField(
            model_name='pond_tb',
            name='preject',
        ),
    ]
