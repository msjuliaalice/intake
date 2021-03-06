# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-20 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intake', '0025_remove_formsubmission_counties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationlogentry',
            name='event_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'opened'), (2, 'referred'), (3, 'processed'), (4, 'deleted'), (5, 'sent confirmation'), (6, 'referred to another org')]),
        ),
    ]
