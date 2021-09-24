from django.urls import path,re_path
from .views import generate_qrcode

urlpatterns = [
    path('qrcode/',generate_qrcode)
]