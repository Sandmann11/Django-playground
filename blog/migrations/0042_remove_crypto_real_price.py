# Generated by Django 3.1.7 on 2021-04-15 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0041_auto_20210415_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='real_price',
        ),
    ]
