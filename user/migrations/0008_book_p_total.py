# Generated by Django 4.2.1 on 2023-06-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_book_p_farmer_book_f_farmer'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_p',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
