# Generated by Django 4.2.1 on 2023-07-03 05:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0014_product_tb_fpayment_product_tb_fstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_feed',
            name='billdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
