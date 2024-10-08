# Generated by Django 5.1 on 2024-09-26 13:17

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('name', models.CharField(max_length=50)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=5)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=20, region=None)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()])),
            ],
        ),
    ]
