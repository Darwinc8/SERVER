# Generated by Django 3.2.21 on 2024-07-19 00:09

import armamento.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armamento',
            name='CIHB',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[armamento.models.validate_09]),
        ),
        migrations.AlterField(
            model_name='armamento',
            name='FOLIO_C',
            field=models.CharField(max_length=20, validators=[armamento.models.validate_AZ_09_Ñ]),
        ),
        migrations.AlterField(
            model_name='armamento',
            name='FOLIO_D',
            field=models.CharField(max_length=20, validators=[armamento.models.validate_AZ_09_Ñ]),
        ),
        migrations.AlterField(
            model_name='armamento',
            name='MATRICULA',
            field=models.CharField(max_length=20, unique=True, validators=[armamento.models.validate_AZ_09_Ñ, armamento.models.validar_sin_acentos]),
        ),
        migrations.AlterField(
            model_name='armamento',
            name='MATRICULA_CANON',
            field=models.CharField(blank=True, max_length=40, null=True, validators=[armamento.models.validate_AZ_09_Ñ]),
        ),
        migrations.AlterField(
            model_name='armamento',
            name='OBSERVACIONES',
            field=models.TextField(validators=[armamento.models.validate_especiales]),
        ),
    ]
