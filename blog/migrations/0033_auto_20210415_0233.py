# Generated by Django 3.1.7 on 2021-04-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_crypto_new_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypto',
            name='new_price',
            field=models.FloatField(max_length=15, null=True),
        ),
    ]
