from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pencil(request):
    return HttpResponse('Please sharp me I am broken')
def sharpner(request):
    return HttpResponse("I don't have sharpness " )
