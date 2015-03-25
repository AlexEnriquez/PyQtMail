# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PyDrill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='destinatario',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mail',
            name='remitente',
            field=models.TextField(max_length=200),
        ),
    ]
