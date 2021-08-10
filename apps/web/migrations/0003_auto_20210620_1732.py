# Generated by Django 3.2.4 on 2021-06-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_slider_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Logo Socio')),
                ('titulo', models.CharField(max_length=150, verbose_name='Nombre Socio')),
                ('descripcion', models.CharField(max_length=250, verbose_name='Descripcion')),
                ('contenido', models.TextField(verbose_name='Contenido')),
            ],
            options={
                'verbose_name': 'Socio',
                'verbose_name_plural': 'Socios',
                'db_table': 'Servicios',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'managed': False, 'verbose_name': 'Slider', 'verbose_name_plural': 'Sliders'},
        ),
    ]
