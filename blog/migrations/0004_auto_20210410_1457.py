# Generated by Django 3.1.7 on 2021-04-10 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='lead',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
