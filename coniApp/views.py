from django.shortcuts import render
from django.http import HttpResponse


def index(request): #cuando el cliente manda algo al servidor (manda algo)
    html="""
    <h1>Soy el index de la app 1</h1>
    <h2>Hola!</h2>
    """
    return HttpResponse(html)



def funcion(request):
    html=""" 
    <h1 style="color:pink">lo que tu quieras</h1>
    <h2>lo que tu quieras</h2>
    <h3>lo que tu quieras</h3>
    <h4>lo que tu quieras</h4>
    """
    return HttpResponse(html)