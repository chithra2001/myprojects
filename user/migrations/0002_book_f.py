# Generated by Django 4.2.1 on 2023-05-31 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_f',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('P_name', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('del_date', models.CharField(max_length=50)),
                ('del_time', models.CharField(max_length=50)),
                ('payment', models.BooleanField(max_length=50)),
                ('accept', models.BooleanField(max_length=50)),
                ('reject', models.BooleanField(max_length=50)),
                ('book', models.BooleanField(max_length=50)),
                ('Uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.u_reg')),
            ],
        ),
    ]