from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from Sibintek_site import settings
from main import views


urlpatterns = [
    path("", include("main.urls")),
    path("doc1", views.documentation_page1, name="doc_page"),
    path("doc2", views.documentation_page2, name="doc_page"),
    path("doc3", views.documentation_page3, name="doc_page"),
    path("crew", views.crew, name="doc_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
