# Generated by Django 2.2.4 on 2023-01-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230125_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nickName',
            field=models.CharField(default='default', max_length=15, verbose_name='昵称'),
        ),
    ]