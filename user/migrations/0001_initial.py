# Generated by Django 2.2.4 on 2023-02-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=10, unique=True, verbose_name='username')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='email')),
                ('headPortrait', models.ImageField(null=True, upload_to='Photos/headPortrait', verbose_name='头像')),
                ('nickName', models.CharField(default='default', max_length=15, verbose_name='昵称')),
                ('phone', models.CharField(blank=True, max_length=128, null=True)),
                ('qq', models.CharField(blank=True, max_length=128, null=True)),
                ('wechat', models.CharField(blank=True, max_length=128, null=True)),
                ('sex', models.CharField(blank=True, choices=[('男', '男'), ('女', '女')], max_length=45, null=True)),
                ('personalSignature', models.CharField(blank=True, max_length=500, null=True, verbose_name='个性签名')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('is_admin', models.BooleanField(default=False, verbose_name='是否管理员')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'db_table': 'home_user_profile',
            },
        ),
    ]
