# Generated by Django 3.1.7 on 2021-04-12 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20210412_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='lus-200.jpg', null=True, upload_to=''),
        ),
    ]
