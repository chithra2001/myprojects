# Generated by Django 4.2.1 on 2023-06-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessor', '0009_pond_tb_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='pond_tb',
            name='paccept',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pond_tb',
            name='ppayment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='pond_tb',
            name='preject',
            field=models.BooleanField(default=False),
        ),
    ]