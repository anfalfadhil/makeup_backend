# Generated by Django 3.2.8 on 2021-10-13 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0003_alter_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tads',
            new_name='tags',
        ),
    ]
