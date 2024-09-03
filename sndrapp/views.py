from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html="""
    <h1>Hola, esta es la pagina inicial</h1>
    """
    return HttpResponse(html)

def fun1(request):
    html="""
    <h1>PAG 2</h1>
    <h2>HIIII!</h2>
    """
    return HttpResponse(html)

# Create your views here.
