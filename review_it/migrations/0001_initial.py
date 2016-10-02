# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-01 17:38
from __future__ import unicode_literals

from django.conf import settings
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
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('auther', models.CharField(blank=True, max_length=30, null=True)),
                ('publisher', models.CharField(blank=True, max_length=30, null=True)),
                ('number_of_reviews', models.IntegerField(default=0)),
                ('average_rating', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=2000)),
                ('star_rating', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('review_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='review_it.Book')),
            ],
        ),
    ]