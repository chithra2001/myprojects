# Generated by Django 4.2.1 on 2023-06-02 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_remove_book_p_total_book_f_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_p',
            name='desc',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='book_p',
            name='lessor',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='book_p',
            name='location',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
