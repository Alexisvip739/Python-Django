# Generated by Django 3.2.5 on 2021-08-04 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listado_Pendiente', '0002_alter_pendientes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendientes',
            name='Horario',
            field=models.TimeField(),
        ),
    ]
