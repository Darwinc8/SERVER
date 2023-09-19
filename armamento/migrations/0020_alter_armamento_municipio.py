# Generated by Django 4.2.3 on 2023-09-18 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos', '0017_delete_armamento'),
        ('armamento', '0019_alter_armamento_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armamento',
            name='MUNICIPIO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='catalogos.municipio'),
        ),
    ]