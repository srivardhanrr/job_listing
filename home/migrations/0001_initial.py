# Generated by Django 5.1.3 on 2024-11-21 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('color_code', models.CharField(default='#6c757d', help_text='Color code in hex format (e.g., #00a0c6)', max_length=7)),
                ('icon', models.CharField(blank=True, help_text='Icon emoji or code (e.g., 👁️ or 🩺)', max_length=50)),
                ('description', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('location_city', models.CharField(max_length=100)),
                ('location_state', models.CharField(max_length=2)),
                ('job_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contract', 'Contract'), ('remote', 'Remote')], max_length=20)),
                ('description', models.TextField()),
                ('salary_range', models.CharField(blank=True, max_length=100)),
                ('application_url', models.URLField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='job_listings', to='home.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
