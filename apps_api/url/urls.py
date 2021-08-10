
from django.urls import path, include,re_path
from apps_api.vistas.vistas import SliderCrearApi,SocioCrearApi,ServiciosCrearApi,ProgramasCrearApi





urlpatterns = [

  	path('slider/crear',SliderCrearApi.as_view()),
  	path('socio/crear',SocioCrearApi.as_view()),
  	path('servicios/crear',ServiciosCrearApi.as_view()),
  	path('programas/crear',ProgramasCrearApi.as_view()),
  

    ]