# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PyDrill', '0002_auto_20150321_2233'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Destinatario',
        ),
        migrations.DeleteModel(
            name='Remitente',
        ),
    ]
