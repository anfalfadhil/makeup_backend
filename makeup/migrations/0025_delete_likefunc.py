# Generated by Django 3.2.8 on 2021-10-22 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0024_post_likes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LikeFunc',
        ),
    ]