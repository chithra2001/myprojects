# Generated by Django 4.2.1 on 2023-06-15 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0007_book_feed_delete_bookpond'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_feed',
            name='packets',
            field=models.IntegerField(null=True),
        ),
    ]