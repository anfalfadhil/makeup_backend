# Generated by Django 3.2.8 on 2021-10-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0004_rename_tads_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images'),
        ),
    ]