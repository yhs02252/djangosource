# Generated by Django 5.1.4 on 2025-01-17 03:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성날짜')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='수정날짜')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogpost', verbose_name='원본글')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'db_table': 'commenttbl',
            },
        ),
    ]
