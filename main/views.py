from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html", context={})


def documentation_page1(request):
    return render(request, "documentation/1.html")


def documentation_page2(request):
    return render(request, "documentation/2.html")


def documentation_page3(request):
    return render(request, "documentation/3.html")


def crew(request):
    return render(request, "crew.html")


def scaners(request):
    return render(request, "documentation/scaners.html")

def lab(request):
    return render(request, "documentation/lab.html")

def alg(request):
    return render(request, "documentation/alg.html")

def video(request):
    return render(request, "video.html")