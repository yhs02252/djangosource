# Generated by Django 5.1.4 on 2025-01-13 07:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_person_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_app',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
