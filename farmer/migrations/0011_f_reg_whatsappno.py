# Generated by Django 4.2.1 on 2023-06-27 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0010_alter_f_reg_experience'),
    ]

    operations = [
        migrations.AddField(
            model_name='f_reg',
            name='whatsappno',
            field=models.CharField(max_length=10, null=True),
        ),
    ]