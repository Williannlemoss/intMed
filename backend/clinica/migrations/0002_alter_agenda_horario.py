# Generated by Django 3.2.3 on 2021-05-26 02:31

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='horario',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), null=True, size=None),
        ),
    ]
