# Generated by Django 3.1.7 on 2021-04-15 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0038_auto_20210415_0331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crypto',
            name='real_price',
        ),
    ]
