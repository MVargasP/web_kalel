from django.shortcuts import render,redirect, get_object_or_404 
from django.views.generic import ListView, DetailView, View,TemplateView
from apps.web.models import Contacto
import os
import shutil, sys 
import qrcode


def generate_qrcode_empresa(request):
    if request.method == "POST":
        buscar = request.POST['dni']
        #print(os.listdir('static/empresa/CRISTO VIENE/'))
        try:
            contenido = os.listdir('static/empresa/{}/TARJETA/'.format(buscar))            
        except Exception as e:
            return render(request,'codigoQr/qr_empresa.html',{"error":"no existe carpeta"})

        """try:
                                    os.remove('static/empresa/{}/QR'.format(buscar))
                                except:
                                    os.mkdir('static/empresa/{}/QR'.format(buscar))"""

        for x in contenido:
            link='https://www.kalelsac.com/static/empresa/{}/TARJETA/{}'.format(buscar,x)
            #print(link)
            img = qrcode.make(link)

            f = open("static/empresa/{}/QR/{}".format(buscar,x), "wb")
            img.save(f)
            f.close()


        try:
            os.remove("static/empresa/{}/comprimido/{}".format(buscar,buscar))
        except:
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
            

            


    
    
        