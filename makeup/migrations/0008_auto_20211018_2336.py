# Generated by Django 3.2.8 on 2021-10-18 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0007_auto_20211014_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('posts', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='makeup.post')),
            ],
        ),
    ]