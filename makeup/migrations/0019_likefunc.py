# Generated by Django 3.2.8 on 2021-10-19 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('makeup', '0018_auto_20211019_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeFunc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('Like', 'Like'), ('Dislike', 'Dislike')], default='Like', max_length=10)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeup.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]