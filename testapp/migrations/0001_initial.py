# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('photo', models.FileField(upload_to=b'photos/%Y/%m/%d/')),
                ('created', models.DateField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('auto_delete', models.BooleanField(default=True, help_text=b'Auto Delete image unoptimized when uploaded.')),
            ],
            options={
                'ordering': ['-created'],
                'verbose_name': 'Photos',
                'verbose_name_plural': 'Detail Photo',
            },
        ),
    ]
