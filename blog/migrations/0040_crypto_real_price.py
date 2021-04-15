# Generated by Django 3.1.7 on 2021-04-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_remove_crypto_real_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='crypto',
            name='real_price',
            field=models.JSONField(default='', verbose_name={'mins': 5, 'price': '62694.39913096'}),
        ),
    ]
