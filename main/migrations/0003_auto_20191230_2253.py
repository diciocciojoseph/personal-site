# Generated by Django 3.0.1 on 2019-12-31 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191230_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.FilePathField(path='main/static/images'),
        ),
    ]
