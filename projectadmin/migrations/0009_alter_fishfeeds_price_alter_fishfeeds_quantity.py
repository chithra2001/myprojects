# Generated by Django 4.2.1 on 2023-06-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectadmin', '0008_alter_fishfeeds_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishfeeds',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='fishfeeds',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
