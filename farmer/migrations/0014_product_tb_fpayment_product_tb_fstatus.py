# Generated by Django 4.2.1 on 2023-06-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0013_product_tb_accept_product_tb_reject'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_tb',
            name='fpayment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product_tb',
            name='fstatus',
            field=models.BooleanField(default=False),
        ),
    ]