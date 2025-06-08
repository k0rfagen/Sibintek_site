from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from Sibintek_site import settings
from main import views

urlpatterns = [
    # Локальные маршруты с понятными URL'ами
    path("", include("main.urls")),
    
    # Маршруты из локальной версии (со старыми путями)
    path('1.html', views.documentation_page1, name='page_1'),
    path('2.html', views.documentation_page2, name='page_2'),
    path('3.html', views.documentation_page3, name='page_3'),
    path('crew.html', views.crew, name='crew'),
    path('scaners.html', views.scaners, name='scaners'),

    # Маршруты из удалённой версии (чистые URL)
    path("doc1", views.documentation_page1, name="doc_page1"),
    path("doc2", views.documentation_page2, name="doc_page2"),
    path("doc3", views.documentation_page3, name="doc_page3"),
    path("crew", views.crew, name="crew_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
