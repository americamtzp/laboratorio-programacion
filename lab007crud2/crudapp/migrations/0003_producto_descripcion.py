# Generated by Django 5.1.1 on 2024-09-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_remove_producto_descripcion_producto_cantidad_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]