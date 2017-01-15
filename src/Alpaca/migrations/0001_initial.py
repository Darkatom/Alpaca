# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-07 23:55
from __future__ import unicode_literals

import Alpaca.file_paths
import Alpaca.storage
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, default=Alpaca.file_paths.no_cover_path, null=True, storage=Alpaca.storage.OverwriteStorage(), upload_to=Alpaca.file_paths.activity_cover_path)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('city', models.TextField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='publication date')),
                ('num_attendants', models.IntegerField(default=0)),
                ('auto_register', models.BooleanField(default=False)),
                ('confirmation_period', models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(3)])),
                ('age_minimum', models.IntegerField(default=0)),
                ('attendants', models.ManyToManyField(blank=True, related_name='attending_activities', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_activities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, default=Alpaca.file_paths.no_cover_path, null=True, storage=Alpaca.storage.OverwriteStorage(), upload_to=Alpaca.file_paths.event_cover_path)),
                ('banner', models.ImageField(blank=True, default=Alpaca.file_paths.no_banner_path, null=True, storage=Alpaca.storage.OverwriteStorage(), upload_to=Alpaca.file_paths.event_banner_path)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=5000)),
                ('city', models.TextField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='publication date')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='start date')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='end date')),
                ('age_minimum', models.IntegerField(default=0)),
                ('num_attendants', models.IntegerField(default=0)),
                ('show_title', models.BooleanField(default=True)),
                ('group_only_attendants', models.BooleanField(default=False)),
                ('auto_register_users', models.BooleanField(default=True)),
                ('auto_register_activities', models.BooleanField(default=False)),
                ('attendants', models.ManyToManyField(blank=True, related_name='attending_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, default='no-logo.png', null=True, storage=Alpaca.storage.OverwriteStorage(), upload_to=Alpaca.file_paths.group_logo_path)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('total_num_members', models.IntegerField(default=0)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
                ('show_email', models.BooleanField(default=True)),
                ('auto_register_users', models.BooleanField(default=False)),
                ('auto_register_activities', models.BooleanField(default=False)),
                ('admin_list', models.ManyToManyField(blank=True, related_name='admin_of', to=settings.AUTH_USER_MODEL)),
                ('member_list', models.ManyToManyField(blank=True, related_name='member_of', to=settings.AUTH_USER_MODEL)),
                ('pending_members', models.ManyToManyField(blank=True, related_name='waiting_groups', to=settings.AUTH_USER_MODEL)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='superuser_of', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='no-avatar.png', null=True, storage=Alpaca.storage.OverwriteStorage(), upload_to=Alpaca.file_paths.user_avatar_path)),
                ('birth_date', models.DateField(verbose_name='date of birth')),
                ('current_token', models.CharField(default='', max_length=100)),
                ('language_preference', models.CharField(default='English', max_length=50)),
                ('show_email', models.BooleanField(default=True)),
                ('show_birthday', models.BooleanField(default=True)),
                ('show_real_name', models.BooleanField(default=True)),
                ('display_name_format', models.CharField(default='nick (full_name)', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
                ('location', models.CharField(max_length=100)),
                ('emails_are_sent', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alpaca.Activity')),
                ('confirmed_attendants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Alpaca.Group'),
        ),
        migrations.AddField(
            model_name='event',
            name='pending_attendants',
            field=models.ManyToManyField(blank=True, related_name='waiting_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_list', to='Alpaca.Event'),
        ),
        migrations.AddField(
            model_name='activity',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activity_list', to='Alpaca.Group'),
        ),
        migrations.AddField(
            model_name='activity',
            name='pending_attendants',
            field=models.ManyToManyField(blank=True, related_name='waiting_activities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='pending_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pending_activities', to='Alpaca.Event'),
        ),
        migrations.AddField(
            model_name='activity',
            name='pending_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pending_activities', to='Alpaca.Group'),
        ),
    ]