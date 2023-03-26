from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """returns homepage of ShadeCompany site"""
    return render(request, 'ShadeKart/homepage.html')
