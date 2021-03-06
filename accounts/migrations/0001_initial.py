# Generated by Django 2.2.5 on 2019-09-11 19:22

import accounts.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10, null=True, verbose_name='gender')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='DOB')),
                ('contact', models.CharField(blank=True, max_length=20, null=True, verbose_name='contact')),
                ('address', models.TextField(blank=True, max_length=200, null=True, verbose_name='address')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='city')),
                ('state', models.CharField(blank=True, max_length=100, null=True, verbose_name='state/province')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('about', models.TextField(blank=True, max_length=300, null=True, verbose_name='about')),
                ('image', models.ImageField(blank=True, null=True, upload_to=accounts.utils.upload_image_path, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
                'ordering': ['-user__date_joined'],
            },
        ),
    ]
