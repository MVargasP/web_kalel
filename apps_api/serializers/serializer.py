from django.urls import path, include
from apps.web.models import Slider,Socio,Servicios,Programas
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('__all__')

class SocioSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(read_only=True)

    class Meta:
        model = Socio
        fields = ('__all__')

class ServiciosSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(read_only=True)

    class Meta:
        model = Servicios
        fields = ('__all__')

class ProgramasSerializer(serializers.ModelSerializer):
    estado = serializers.BooleanField(read_only=True)

    class Meta:
        model = Programas
        fields = ('__all__')