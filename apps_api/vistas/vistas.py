from rest_framework import generics, permissions,status
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from apps.web.models import Slider,Socio,Servicios,Programas
from apps_api.serializers.serializer import SliderSerializer,SocioSerializer,ServiciosSerializer,ProgramasSerializer

#from knox.models import AuthToken
from rest_framework.generics import (ListAPIView,CreateAPIView,
    RetrieveAPIView,DestroyAPIView,
    UpdateAPIView,RetrieveUpdateAPIView)


# ViewSets define the view behavior.
class SliderCrearApi(CreateAPIView,ListAPIView):
	permission_classes = [permissions.AllowAny ]
	queryset = Slider.objects.all()
	serializer_class = SliderSerializer

class SocioCrearApi(CreateAPIView,ListAPIView):
	permission_classes = [permissions.AllowAny ]
	queryset = Socio.objects.all()
	serializer_class = SocioSerializer

class ServiciosCrearApi(CreateAPIView,ListAPIView):
	permission_classes = [permissions.AllowAny ]
	queryset = Servicios.objects.all()
	serializer_class = ServiciosSerializer

class ProgramasCrearApi(CreateAPIView,ListAPIView):
	permission_classes = [permissions.AllowAny ]
	queryset = Programas.objects.all()
	serializer_class = ProgramasSerializer