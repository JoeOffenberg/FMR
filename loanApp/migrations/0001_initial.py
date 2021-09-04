# Generated by Django 3.1.5 on 2021-09-03 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginApp', '0002_auto_20210902_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='loanCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_name', models.CharField(max_length=250)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='loanRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('reason', models.CharField(max_length=250)),
                ('is_approved', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loanApp.loancategory')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginApp.customersignup')),
            ],
        ),
    ]