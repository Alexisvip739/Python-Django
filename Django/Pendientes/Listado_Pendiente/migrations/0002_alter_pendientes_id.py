# Generated by Django 3.2.5 on 2021-08-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Listado_Pendiente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendientes',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
