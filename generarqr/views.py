from django.shortcuts import render,redirect, get_object_or_404 
from django.views.generic import ListView, DetailView, View,TemplateView
from apps.web.models import Contacto
import os
import shutil, sys 
import qrcode
img = qrcode.make("Hola desde Recursos Python!")
f = open("output.png", "wb")
img.save(f)
f.close()

def generate_qrcode_empresa(request):
    if request.method == "POST":
        buscar = request.POST['dni']
        #print(os.listdir('static/empresa/CRISTO VIENE/'))
        contenido = os.listdir('static/empresa/{}/TARJETA/'.format(buscar))
        for x in contenido:
            f = open("static/empresa/{}/QR/{}.png".format(buscar,x), "wb")
            img.save(f)
            f.close()

        archivo_zip = shutil.make_archive("static/empresa/{}/comprimido/{}".format(buscar,buscar), 
                                  "zip", 
                                  "static/empresa/{}/QR".format(buscar))
        ruta="static/empresa/{}/comprimido/{}".format(buscar,buscar)
        contexto = {
                'ruta':ruta }
        return render(request,'codigoQr/qr_empresa.html',contexto)

    else:

        return render(request,'codigoQr/qr_empresa.html')



def generate_qrcode(request):
    if request.method == "POST":
        buscar = request.POST['dni']
        url='https://www.kalelsac.com/static/codigoqr/'
  
        ruta="https://www.kalelsac.com/static/codigoqr/{}".format(buscar)
        print(ruta)
        
        contexto = {
                'ruta':ruta }
        return render(request,'codigoQr/codigos.html',contexto)

    else:

        return render(request,'codigoQr/codigos.html')
            

            


    
    
        