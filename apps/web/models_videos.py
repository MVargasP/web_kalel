from django.db import models
from ckeditor.fields import RichTextField 

class TemaVideo(models.Model):
	titulo = models.CharField('Titulo del Video' , max_length=150, unique=True)
	descripcion = models.CharField('Descripcion',max_length=300,null=True,blank=True)
	encuesta_link = models.URLField('Link Encuesta',null=True,blank=True,max_length=200 )
	imagen_referencial= models.ImageField('Subir Imagen',upload_to='static/tema/imagen',blank=True,null=True)
	slug = models.SlugField('Slug',max_length=150,unique=True, null=True,blank=True)
	publicado = models.BooleanField('Publicado / No Publicado',default=False)
	estado = models.BooleanField('Estado', default=True)

	
  
	class Meta:
		verbose_name='Tema Video'
		verbose_name_plural='Temas Videos'
		managed = False
		db_table = 'video_temavideo'
		

	def __str__(self):
		return self.slug


class Video(models.Model):
	titulo = models.CharField('Titulo del Video' , max_length=150, unique=True)
	slug = models.SlugField('Slug',max_length=150,unique=True)
	descripcion = models.CharField('Descripcion',max_length=200)
	#autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
	link_incorporado= models.FileField('Subir Video',upload_to='static/videos/video',blank=True,null=True) 
	contenido = RichTextField()
	imagen_referencial = models.ImageField('Imagen Referencial', max_length=150,null=True,blank=True)
	publicado = models.BooleanField('Publicado / No Publicado',default=False)
	fecha_publicacion= models.DateField('Fecha de Publicación')
	tema=models.ForeignKey(TemaVideo,related_name='videotema', on_delete=models.CASCADE)
	video=models.CharField('link-Vimeo',max_length=200, blank=True,null=True)
	estado = models.BooleanField('Estado', default=True)

	#cargarvideo = models.FileField('Subir Video',upload_to='videos')

	class Meta:
		verbose_name='Video'
		verbose_name_plural='Videos'
		managed = False
		db_table = 'video_video'

	def __str__(self):
		return str(self.titulo)