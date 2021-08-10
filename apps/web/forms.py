from django.forms import ModelForm
from .models import  Contacto
class ContactoForm(ModelForm):
	class Meta:
		model = Contacto
		fields= [
		'nombre',
		'apellidos',
		'correo',
		'asunto',
		'mensaje',
		]

		labels= {
		'nombre': 'Nombre' ,
		'apellidos': 'Apellidos',
		'correo': 'Correo',
		'asunto':'Asunto ' ,
		'mensaje':'Mensaje' ,

		}