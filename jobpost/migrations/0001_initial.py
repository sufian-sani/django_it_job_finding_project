# Generated by Django 3.1.3 on 2022-03-05 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=17)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.CharField(default=models.CharField(max_length=50), max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('salary', models.FloatField()),
                ('details', models.TextField()),
                ('available', models.BooleanField()),
                ('category', models.CharField(choices=[('Student', 'Student'), ('Fresher', 'Fresher'), ('Experience', 'Experience'), ('Experience Plus', 'Experience Plus')], max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='default.jpg', upload_to='jobpost/images')),
                ('Expertise', multiselectfield.db.fields.MultiSelectField(choices=[('web_development', 'Web Development'), ('web_design', 'Web Design'), ('graphich_design', 'Graphich Design'), ('seo', 'Search Engine Optimization'), ('digital_merketing', 'Degital Merketing'), ('apps_development', 'App Development'), ('programing', 'Programing'), ('game_development', 'Game Development'), ('other', 'Other')], default='other', max_length=115)),
                ('Skill', multiselectfield.db.fields.MultiSelectField(choices=[('social_media_marketing', 'Social media marketing'), ('search_engine_optimization', 'Search Engine Optimization'), ('adobe_photoshop', 'Adobe Photoshop'), ('html', 'html'), ('css', 'css'), ('javascript', 'javascript'), ('wordpress', 'wordpress'), ('php', 'php'), ('python', 'python'), ('go', 'go'), ('java', 'java'), ('c++', 'c++'), ('other', 'Other')], default='other', max_length=124)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('likes', models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('views', models.ManyToManyField(related_name='post_views', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='jobpost/images')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='jobpost.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobpost.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobpost.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
