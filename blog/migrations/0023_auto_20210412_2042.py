# Generated by Django 3.1.7 on 2021-04-12 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20210412_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='static/img/lus-200.jpg', upload_to=''),
        ),
    ]
