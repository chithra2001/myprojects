# Generated by Django 4.2.1 on 2023-06-19 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_book_f_avgwght'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='u_reg',
            name='Gender',
        ),
    ]
