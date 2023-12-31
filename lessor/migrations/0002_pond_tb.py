# Generated by Django 4.2.1 on 2023-05-31 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pond_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=20)),
                ('plot_area', models.CharField(max_length=20)),
                ('breadth', models.CharField(max_length=20)),
                ('length', models.CharField(max_length=20)),
                ('facing', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=50)),
                ('Description', models.CharField(max_length=50)),
                ('L_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessor.l_reg')),
            ],
        ),
    ]
