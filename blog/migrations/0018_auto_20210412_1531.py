# Generated by Django 3.1.7 on 2021-04-12 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20210410_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='/static/img/lus-200.jpg', null=True, upload_to=''),
        ),
    ]