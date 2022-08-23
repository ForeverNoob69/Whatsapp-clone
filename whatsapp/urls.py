from re import template
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('',TemplateView.as_view(template_name='index.html')),
]
