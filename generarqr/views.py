from django.shortcuts import render,redirect, get_object_or_404 
from django.views.generic import ListView, DetailView, View,TemplateView
from apps.web.models import Contacto


"""class generate_qrcode(ListView):
    model=Contacto
   
    def post(self,request,*args,**kwargs):
        buscar= request.POST['dni']
       
        if buscar:
            print(buscar)

    
        contexto = {
            'fecha_actual':now,
            'dni':placa,
    
            'busqueda':buscar,

        }
        return render(request,'codigoQr/codigos.html',contexto)

   
"""


def generate_qrcode(request):
    if request.method == "POST":
        buscar = request.POST['dni']
        url='https://www.kalelsac.com/static/codigoqr/'
  
        ruta=url+buscar
        
        contexto = {
                'ruta':ruta }
        return render(request,'codigoQr/codigos.html',contexto)

    else:

        return render(request,'codigoQr/codigos.html')
            

            


    
    
        