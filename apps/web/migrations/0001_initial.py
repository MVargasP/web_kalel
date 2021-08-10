# Generated by Django 3.2.4 on 2021-06-20 15:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Imagen Blog')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulo Blog')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Slug')),
                ('contenido', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Contenido')),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
                'db_table': 'web_blog',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('correo', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('mensaje', ckeditor.fields.RichTextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'db_table': 'web_contacto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
                'db_table': 'web_redessociales',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Logo Socio')),
                ('titulo', models.CharField(max_length=150, verbose_name='Nombre Socio')),
            ],
            options={
                'verbose_name': 'Socio',
                'verbose_name_plural': 'Socios',
                'db_table': 'web_socio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('correo', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
                'db_table': 'web_suscriptor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nosotros', models.TextField(verbose_name='Nosotros')),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Web',
                'verbose_name_plural': 'Webs',
                'db_table': 'web_web',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('imagen_principal', models.ImageField(upload_to='', verbose_name='Imagen Slider')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
                'db_table': 'web_slider',
                'managed': False,
                
            },
        ),
    ]
