# Generated by Django 3.1.3 on 2022-01-18 12:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tuition', '0009_auto_20220114_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.ManyToManyField(related_name='post_views', to=settings.AUTH_USER_MODEL),
        ),
    ]
