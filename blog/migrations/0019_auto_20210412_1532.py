# Generated by Django 3.1.7 on 2021-04-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20210412_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/img/lus-200.jpg', null=True, upload_to=''),
        ),
    ]
