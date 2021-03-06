# Generated by Django 3.2.9 on 2021-11-27 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contributor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VettingDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bio', models.CharField(max_length=240)),
                ('email', models.EmailField(max_length=240)),
                ('website', models.URLField(max_length=240)),
                ('avatar_url', models.URLField(max_length=240)),
                ('location', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=80)),
                ('company', models.CharField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='vetter_to_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SignedOff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('device_id', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('upvoted', models.BooleanField(default=False)),
                ('downvoted', models.BooleanField(default=False)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signed_off_to_user', to=settings.AUTH_USER_MODEL)),
                ('repo_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributor_to_repo_model', to='contributor.repomodel')),
            ],
        ),
        migrations.CreateModel(
            name='RepositoryURL',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('discussion_url', models.CharField(max_length=240)),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repository_url_to_user', to=settings.AUTH_USER_MODEL)),
                ('repo_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repository_url_to_repo', to='contributor.repomodel')),
            ],
        ),
    ]
