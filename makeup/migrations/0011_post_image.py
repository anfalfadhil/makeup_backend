# Generated by Django 3.2.8 on 2021-10-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0010_auto_20211019_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
    ]
