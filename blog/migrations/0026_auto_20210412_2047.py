# Generated by Django 3.1.7 on 2021-04-12 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20210412_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='lus-200.jpg', upload_to=''),
        ),
    ]
