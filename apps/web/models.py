from django.db import models
from ckeditor.fields import RichTextField 

class ModeloBase(models.Model):
	id = models.AutoField(primary_key=True)
	estado = models.BooleanField('Estado', default=True)
	fecha_creacion = models.DateField('Fecha de Creacion',auto_now=False,auto_now_add=True) 
	fecha_modificacion = models.DateField('Fecha de Modificacion',auto_now=True,auto_now_add=False)
	fecha_eliminacion = models.DateField('Fecha de Eliminacion',auto_now=True,auto_now_add=False)

	class Meta:
		abstract = True
 

class Contacto(ModeloBase):
    nombre = models.CharField('Nombre', max_length = 100)
    apellidos = models.CharField('Apellidos', max_length = 150)
    correo = models.EmailField('Correo Electrónico', max_length = 200)
    asunto = models.CharField('Asunto', max_length = 100)
    mensaje = RichTextField('Mensaje')

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        managed = False
        db_table = 'web_contacto'

    def __str__(self):
        return self.asunto
class Blog(ModeloBase):
    imagen=models.ImageField('Imagen Blog',upload_to='web/blog')
    titulo=models.CharField('Titulo Blog',max_length=200)
    descripcion=models.CharField('Titulo Blog',max_length=300,blank=True,null=True)
    slug = models.SlugField('Slug',max_length=150,unique=True)

    contenido=RichTextField('Contenido',blank=True,null=True)
    


    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        managed = False
        db_table = 'web_blog'
    def __str__(self):
        return self.titulo
class Web(ModeloBase):
    nosotros = models.CharField('Nosotros',max_length=350)
    telefono = models.CharField('Teléfono', max_length = 10)
    email = models.EmailField('Correo Electrónico', max_length = 200)
    direccion = models.CharField('Dirección', max_length = 200)

    class Meta:
        verbose_name = 'Web'
        verbose_name_plural = 'Webs'
        managed = False
        db_table = 'web_web'

    def __str__(self):
        return self.nosotros

class RedesSociales(ModeloBase):
    facebook = models.URLField('Facebook')
    twitter = models.URLField('Twitter',null=True,blank=True)
    instagram = models.URLField('Instagram',null=True,blank=True)

    class Meta:
        verbose_name = 'Red Social'
        verbose_name_plural = 'Redes Sociales'
        managed = False
        db_table = 'web_redessociales'

    def __str__(self):
        return self.facebook

class Suscriptor(ModeloBase):
    correo = models.EmailField('Correo Electrónico', max_length = 200)

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
        managed = False
        db_table = 'web_suscriptor'

    def __str__(self):
        return self.correo

class Slider(ModeloBase):
    imagen_principal=models.ImageField('Imagen Slider',upload_to='web/slider')
    titulo = models.CharField('Titulo', max_length=150)
    descripcion = models.CharField('Descripcion', max_length=250)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE,db_column='blog_id',blank=True,null=True)


    class Meta:
      verbose_name = 'Slider'
      verbose_name_plural = 'Sliders'
      managed = False
      db_table = 'web_slider'
    def __str__(self):
          return self.titulo

class Socio(ModeloBase):
    imagen=models.ImageField('Logo Socio',upload_to='web/socio')
    titulo = models.CharField('Nombre Socio', max_length=150)
    web = models.URLField('Direccion Web')

    class Meta:
      verbose_name = 'Socio'
      verbose_name_plural = 'Socios'
      managed = False
      db_table = 'web_socio'
    def __str__(self):
          return self.titulo



class Servicios(models.Model):
    imagen=models.ImageField('Logo Socio',upload_to='web/servicios')
    titulo = models.CharField('Nombre Socio', max_length=150)
    descripcion = models.CharField('Descripcion', max_length=250)
    contenido = models.TextField('Contenido')
    fecha_creacion = models.DateField(auto_now=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Socio'
        verbose_name_plural = 'Socios'
        managed = False
        db_table = 'Servicios'
    def __str__(self):
        return self.titulo

        


class Programas(models.Model):
    imagen=models.ImageField('Programa',null=True)
    nombre = models.CharField('Nombre Programa', max_length=150)
    url = models.URLField('Link', max_length=250)
    fecha_creacion = models.DateField(auto_now=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Programas'
        verbose_name_plural = 'Programas'
        managed = False
        db_table = 'Programas'
    def __str__(self):
        return self.titulo