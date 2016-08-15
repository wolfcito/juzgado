# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afectado', '0003_auto_20160815_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='afectado',
            old_name='apellido',
            new_name='apellido_afectado',
        ),
        migrations.RenameField(
            model_name='afectado',
            old_name='direccion',
            new_name='direccion_afectado',
        ),
        migrations.RenameField(
            model_name='afectado',
            old_name='nombre',
            new_name='nombre_afectado',
        ),
    ]
