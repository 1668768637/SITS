# Generated by Django 2.2.4 on 2023-03-05 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='postId',
            new_name='post',
        ),
    ]
