# Generated by Django 3.2.8 on 2021-10-19 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0019_likefunc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likefunc',
            old_name='posts',
            new_name='post',
        ),
    ]