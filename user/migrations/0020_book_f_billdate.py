# Generated by Django 4.2.1 on 2023-07-03 04:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_book_f_rate_book_f_review_delete_fishrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_f',
            name='billdate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]