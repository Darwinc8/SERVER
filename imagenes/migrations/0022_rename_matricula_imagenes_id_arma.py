# Generated by Django 3.2.21 on 2023-10-30 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0021_rename_id_arma_imagenes_matricula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagenes',
            old_name='MATRICULA',
            new_name='ID_ARMA',
        ),
    ]