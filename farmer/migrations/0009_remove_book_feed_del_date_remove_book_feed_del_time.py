# Generated by Django 4.2.1 on 2023-06-19 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0008_book_feed_packets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_feed',
            name='del_date',
        ),
        migrations.RemoveField(
            model_name='book_feed',
            name='del_time',
        ),
    ]
