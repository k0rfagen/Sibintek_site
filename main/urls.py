from django.urls import include

from Sibintek_site.urls import urlpatterns

urlpatterns = [
    path('', include('main.urls')),
]