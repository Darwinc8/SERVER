# Generated by Django 4.2.3 on 2023-09-18 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armamento', '0015_alter_armamento_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armamentolog',
            name='id_alterna',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=10),
        ),
        migrations.AlterField(
            model_name='armamentolog',
            name='usuario',
            field=models.CharField(max_length=50),
        ),
    ]