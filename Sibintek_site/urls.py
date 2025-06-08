from django.contrib import admin
from django.urls import path
from main.views import (
    index,
    documentation_page1,
    documentation_page2,
    documentation_page3,
    crew,
    scaners,  # взято из локальной версии (HEAD)
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("documentation/1.html", documentation_page1, name="page_1"),
    path("documentation/2.html", documentation_page2, name="page_2"),
    path("documentation/3.html", documentation_page3, name="page_3"),
    path("crew.html", crew, name="crew"),
    path("documentation/scaners.html", scaners, name="scaners"),  # маршрут из локальной версии
]
