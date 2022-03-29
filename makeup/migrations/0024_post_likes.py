# Generated by Django 3.2.8 on 2021-10-22 12:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('makeup', '0023_comments_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='bposts', to=settings.AUTH_USER_MODEL),
        ),
    ]