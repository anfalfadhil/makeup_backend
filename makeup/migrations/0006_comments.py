# Generated by Django 3.2.8 on 2021-10-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0005_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]