# Generated by Django 5.1.1 on 2024-09-28 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0003_producto_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(),
        ),
    ]