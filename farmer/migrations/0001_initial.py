# Generated by Django 4.2.1 on 2023-05-22 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='f_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_name', models.CharField(max_length=20)),
                ('license_id', models.CharField(max_length=20)),
                ('House_name', models.CharField(max_length=50)),
                ('Street', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=50)),
                ('Phoneno', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('experience', models.CharField(max_length=20)),
            ],
        ),
    ]