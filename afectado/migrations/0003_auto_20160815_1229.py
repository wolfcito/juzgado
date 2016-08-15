# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afectado', '0002_auto_20160813_1141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='afectado',
            old_name='telf_afecto',
            new_name='telf_afectado',
        ),
    ]
