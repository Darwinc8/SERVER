# Generated by Django 3.2.21 on 2023-11-01 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armamento', '0022_auto_20231030_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armamentolog',
            name='cihb',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
