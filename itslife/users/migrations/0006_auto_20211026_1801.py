# Generated by Django 3.2.8 on 2021-10-26 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cover_pic',
            field=models.ImageField(default='default_cover.jfif', upload_to='cover_pics'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='default_user.jfif', upload_to='profile_pics'),
        ),
    ]
