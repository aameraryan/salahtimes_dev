# Generated by Django 2.2 on 2020-01-26 18:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('attribute_name', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('pincode', models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(limit_value=100000), django.core.validators.MaxValueValidator(limit_value=999999)])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localities.City')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
            },
        ),
    ]
