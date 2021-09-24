from django.urls import path,re_path
from .views import generate_qrcode,generate_qrcode_empresa

urlpatterns = [
    path('qrcode/',generate_qrcode),
    path('qr_empresa/',generate_qrcode_empresa)
]