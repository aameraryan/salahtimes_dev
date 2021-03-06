# Generated by Django 2.2 on 2020-01-26 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Masjid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField(blank=True)),
                ('extra_info', models.TextField(blank=True)),
                ('fajar', models.TimeField()),
                ('zuhar', models.TimeField()),
                ('asar', models.TimeField()),
                ('maghrib', models.TimeField()),
                ('isha', models.TimeField()),
                ('juma', models.TimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localities.Area')),
            ],
            options={
                'verbose_name': 'Masjid',
                'verbose_name_plural': 'Masajid',
            },
        ),
    ]
