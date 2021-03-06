# Generated by Django 3.2.8 on 2021-10-13 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='blog_images')),
                ('date', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(blank=True)),
                ('slug', models.SlugField(blank=True, default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeup.author')),
            ],
        ),
    ]
