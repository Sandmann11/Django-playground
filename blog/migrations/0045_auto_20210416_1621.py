# Generated by Django 3.1.7 on 2021-04-16 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20210416_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='Generic Title', max_length=225),
        ),
    ]
