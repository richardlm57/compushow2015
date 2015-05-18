# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compushow_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominacion',
            name='nominado',
            field=models.ForeignKey(to='compushow_app.Computista', default=''),
            preserve_default=False,
        ),
    ]
