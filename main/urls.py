from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from Sibintek_site import settings
from main import views


urlpatterns = [
    path('', include('main.urls')),
    path('1.html', views.documentation_page1, name='doc_page')
    path('2.html', views.documentation_page2, name='doc_page')
    path('3.html', views.documentation_page3, name='doc_page')
    path('crew.html', views.crew, name='doc_page')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)