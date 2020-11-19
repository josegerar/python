# Generated by Django 3.1.3 on 2020-11-19 01:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sustancia',
            name='fecha_creacion',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 18, 20, 57, 54, 389690)),
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sustancia_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.sustancia')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
                'db_table': 'inventario',
                'ordering': ['id'],
            },
        ),
    ]
