# Generated by Django 4.2.1 on 2023-06-23 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_delete_book_p'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_f',
            name='Grade',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
