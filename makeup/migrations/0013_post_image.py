# Generated by Django 3.2.8 on 2021-10-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0012_auto_20211019_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='blog_images'),
        ),
    ]
