# Generated by Django 3.2.8 on 2021-10-27 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='liked',
            new_name='liked_by',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='liked',
            new_name='liked_by',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='shared',
            new_name='shared_by',
        ),
    ]
