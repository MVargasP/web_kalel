from .models import  RedesSociales,Web, Slider , Socio, Blog
from django.core.paginator import Paginator
from django.shortcuts import render,redirect, get_object_or_404 


def obtenerRedes():
    return RedesSociales.objects.filter(estado = True).latest('fecha_creacion')

def obtenerWeb():
    return Web.objects.filter(estado = True).latest('fecha_creacion')

def obtenerMunicipalidad():
	return Socio.objects.filter(estado=True)

def obtenerBlog():
	blog= Blog.objects.all().first()
	if blog:
		return Blog.objects.filter(estado=True)
	

 


 


 
