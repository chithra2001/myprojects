# Generated by Django 4.2.1 on 2023-06-01 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_book_f_accept_alter_book_f_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_f',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
