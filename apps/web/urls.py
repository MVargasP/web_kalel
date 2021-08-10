from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import FormularioContacto,Index,Nosotros,BlogPrincipal ,DetalleBlog,ServicioVIEW
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
 	 path('contacto/',FormularioContacto.as_view(), name = 'contacto'),
 	 path('',Index.as_view(), name = 'inicio'),
 	 path('nosotros/',Nosotros.as_view(), name = 'nosotros'),
 	 path('blog/',BlogPrincipal.as_view(), name = 'blog'),
   	 path('blog/<slug:slug>/',DetalleBlog.as_view(), name = 'detalleblog'), 
   	 path('servicios/',ServicioVIEW.as_view(), name = 'servicio'), 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)