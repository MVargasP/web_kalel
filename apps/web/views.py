from django.shortcuts import render,redirect, get_object_or_404

from django.views.generic import ListView, DetailView, View
from .models import RedesSociales,Web,Slider,Contacto,Blog,Servicios,Socio,Programas
from .models_videos import Video, TemaVideo
from apps.web.utilities import *
from .forms import ContactoForm
#from apps.video.utilities import *
from django.core.paginator import Paginator
from django.db.models import Q

class ServicioVIEW(ListView):

    def get(self,request,*args,**kwargs):
        servicios = Servicios.objects.all().filter(estado=True)
        cursos= TemaVideo.objects.all().filter(estado=True)

        
        if obtenerBlog():
            paginatorblog = Paginator(obtenerBlog(),1)
            pageblog = request.GET.get('page') 
            paginasblog = paginatorblog.get_page(pageblog)  
            blog_reciente=obtenerBlog().latest('fecha_creacion')

        else: 
            blog_reciente=obtenerBlog()
            paginasblog=None

        contexto = {
            'servicios': servicios,
            'cursos': cursos,
            'sociales': obtenerRedes(),
            'nosotros': obtenerWeb(),
            'blog':obtenerBlog(),
            'listar_blog': paginasblog,
            'ultimoblog':blog_reciente,
             

        }
        return render(request,'web/services.html',contexto)
class BlogPrincipal(ListView):
     def get(self,request,*args,**kwargs):


        servicios = Servicios.objects.all()[:6]
        socio = Socio.objects.all()
        cursos= TemaVideo.objects.all().filter(estado=True)
        programas= Programas.objects.all().filter(estado=True)
        nosotros = Web.objects.all().filter(estado=True).first()

        if obtenerBlog():
            paginatorblog = Paginator(obtenerBlog(),5)
            pageblog = request.GET.get('page') 
            paginasblog = paginatorblog.get_page(pageblog)  
      

        else: 
            paginasblog=None
 
        contexto = {

            'socios':socio,
            'cursos':cursos,
            'programas':programas,
            'nosotros':nosotros,
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),      
            'blog': paginasblog,
         
             

        }
        return render(request,'web/blog.html',contexto)

class DetalleBlog(DetailView): 
    def get(self,request,slug,*args,**kwargs):

        servicios = Servicios.objects.all()[:6]
        socio = Socio.objects.all()
        cursos= TemaVideo.objects.all().filter(estado=True)
        programas= Programas.objects.all().filter(estado=True)
        nosotros = Web.objects.all().filter(estado=True).first()

        blog = get_object_or_404(Blog,slug=slug)
        blog = Blog.objects.get(slug=slug)

        paginator = Paginator(listarVideos(),2)
        page = request.GET.get('page')  
        paginas = paginator.get_page(page)  
 
        paginatorblog = Paginator(obtenerBlog(),1)
        pageblog = request.GET.get('page')  
        paginasblog = paginatorblog.get_page(pageblog)  

             

        contexto = {
            'socios':socio,
            'cursos':cursos,
            'programas':programas,
            'nosotros':nosotros,

            'slug': blog,
            'blog':obtenerBlog(),
            'listar': paginas,
            'listar_blog': paginasblog,
                         
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),

        }     
        return render(request, 'web/blog-single.html',contexto ) 



class FormularioContacto(View):
    def get(self,request,*args,**kwargs):
        form = ContactoForm()
        nosotros = Web.objects.all().filter(estado=True).first()

        contexto = {
            'sociales': obtenerRedes(),
			'nosotros': nosotros,
            'form':form,

        }
        return render(request,'web/contact.html',contexto)

    def post(self,request,*args,**kwargs):
        form = ContactoForm(request.POST)      

        if form.is_valid():
            form.save()
            return redirect('contacto')
        else:
            contexto = {
                'form':form,
            }
            return render(request,'web/login.html',contexto)

"""class Index(ListView): 
    def get(self,request,*args,**kwargs):
        slider = Slider.objects.filter( estado=True )
        slider = Slider.objects.filter( estado=True )
 
         
        contexto = {
             
            'principal':slider,
            'municipalidad':obtenerMunicipalidad(),
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),
            'blog':obtenerBlog(),
            'ultimoblog':obtenerBlog().latest('fecha_creacion'),
            
        } 
        return render(request, 'encuesta/web/index.html',contexto )"""


class Nosotros(ListView):
    
    def get(self,request,*args,**kwargs):
        servicios = Servicios.objects.all()[:6]
        socio = Socio.objects.all()
        cursos= TemaVideo.objects.all().filter(estado=True)
        programas= Programas.objects.all().filter(estado=True)
        nosotros = Web.objects.all().filter(estado=True).first()

        contexto= {
            
            'socios':socio,
            'cursos':cursos,
            'programas':programas,
            'nosotros':nosotros,
            'web': obtenerWeb(),
            #'videos': listarVideos(),
        }
        return render(request, 'web/about.html',contexto )


class Index(ListView): 
    def get(self,request,*args,**kwargs):
        slider_one = Slider.objects.filter( estado=True ).first()
        servicios = Servicios.objects.filter(estado=True)[:6]
        socio = Socio.objects.all()
        cursos= TemaVideo.objects.all().filter(estado=True)
        programas= Programas.objects.all().filter(estado=True)
        nosotros = Web.objects.all().filter(estado=True).first()
        if slider_one:
            slider_all = Slider.objects.filter(~Q(id=slider_one.id),estado=True)
        else:
            slider_all=None
        
        contexto = {
               
            'slider_one':slider_one,
            'slider_all':slider_all,
            'socios':socio,
            'cursos':cursos,
            'programas':programas,
            'nosotros':nosotros,
            'municipalidad':obtenerMunicipalidad(),
            'sociales': obtenerRedes(),
            'web': obtenerWeb(),
            'blog':obtenerBlog(),
            'ultimoblog':obtenerBlog(),
            'servicios':servicios

            #.latest('fecha_creacion'),
            
        } 
        return render(request, 'web/index.html',contexto )