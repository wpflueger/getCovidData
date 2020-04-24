import re
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "data/home.html")


def about(request):
    return render(request, "data/about.html")


def contact(request):
    return render(request, "data/contact.html")
