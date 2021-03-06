# Generated by Django 3.2.3 on 2021-05-25 04:44

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('crm', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.especialidade')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('horario', models.TimeField()),
                ('data_agendamento', models.DateTimeField(auto_now=True)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('horario', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(), size=None)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
    ]
