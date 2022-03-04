# Generated by Django 3.1.3 on 2022-03-03 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tuition', '0013_auto_20220121_2233'),
        ('session', '0004_auto_20220304_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', multiselectfield.db.fields.MultiSelectField(choices=[('remote', 'Remote'), ('Onsite', 'On site')], max_length=100)),
                ('approach', multiselectfield.db.fields.MultiSelectField(choices=[('web_development', 'Web Development'), ('web_design', 'Web Design'), ('graphich_design', 'Graphich Design'), ('seo', 'Search Engine Optimization'), ('digital_merketing', 'Degital Merketing'), ('apps_development', 'App Development'), ('programing', 'Programing'), ('game_development', 'Game Development')], max_length=100)),
                ('medium', multiselectfield.db.fields.MultiSelectField(choices=[('social_media_marketing', 'Social media marketing'), ('search_engine_optimization', 'Search Engine Optimization'), ('adobe_photoshop', 'Adobe Photoshop'), ('html', 'html'), ('css', 'css'), ('javascript', 'javascript'), ('wordpress', 'wordpress'), ('php', 'php'), ('python', 'python'), ('go', 'go'), ('java', 'java'), ('c++', 'c++')], max_length=100)),
                ('salary', models.CharField(max_length=100)),
                ('days_per_week', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('in_job', 'In Job')], max_length=100)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district', to='tuition.district')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='jobprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='TuitionProfile',
        ),
    ]