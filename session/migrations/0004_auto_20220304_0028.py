# Generated by Django 3.1.3 on 2022-03-03 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_auto_20220304_0026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='profession',
            new_name='category',
        ),
    ]
