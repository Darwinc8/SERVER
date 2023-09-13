# Generated by Django 4.2.3 on 2023-09-08 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('armamento', '0005_armamento_cuip_responsable'),
    ]

    operations = [
        migrations.AddField(
            model_name='armamento',
            name='ultima_modificacion',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='armamento',
            name='usuario',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]