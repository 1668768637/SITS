# Generated by Django 2.2.4 on 2023-01-26 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0009_auto_20230126_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='publishTime',
        ),
    ]