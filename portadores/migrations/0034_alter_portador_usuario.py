# Generated by Django 4.2.3 on 2023-09-07 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portadores', '0033_portadorlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portador',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]