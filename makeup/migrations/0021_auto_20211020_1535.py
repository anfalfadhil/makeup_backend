# Generated by Django 3.2.8 on 2021-10-20 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0020_rename_posts_likefunc_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
    ]
