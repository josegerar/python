# Generated by Django 3.1.3 on 2020-11-19 01:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sustancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de sustancia')),
                ('fecha_creacion', models.DateTimeField(default=datetime.datetime(2020, 11, 18, 20, 42, 54, 532022))),
                ('url_documentacion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Sustancia',
                'verbose_name_plural': 'Sustancias',
                'db_table': 'sustancia',
                'ordering': ['id'],
            },
        ),
    ]