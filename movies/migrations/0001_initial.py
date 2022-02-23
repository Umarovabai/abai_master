# Generated by Django 4.0 on 2022-02-23 08:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('actor', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=70)),
                ('img', models.ImageField(null=True, upload_to='images')),
                ('description', models.TextField()),
                ('body', models.CharField(max_length=140)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='films', to='movies.category')),
            ],
        ),
        migrations.CreateModel(
            name='MovieReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('rating', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='account.user')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='MoviePlay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film', models.FileField(blank=True, null=True, upload_to='videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked', to='account.user')),
            ],
            options={
                'unique_together': {('movie', 'user')},
            },
        ),
    ]
