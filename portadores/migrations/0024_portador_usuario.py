# Generated by Django 4.2.3 on 2023-08-31 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portadores', '0023_remove_portador_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='portador',
            name='usuario',
            field=models.CharField(default='x', max_length=30),
        ),
    ]