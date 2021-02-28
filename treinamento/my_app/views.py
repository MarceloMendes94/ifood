from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from my_app.models import *
import json

# Create your views here.
def index(request):
    return HttpResponse("<h1>API</h1>")


def listar_lanchonetes(request):
    lanchonetes = Lanchonete.objects.values(
        'nome',
        'endereco__estado',
        'endereco__cidade',
        'telefone').all()
    lanchonetes=list(lanchonetes)
    return JsonResponse({"result":lanchonetes},  safe=False, json_dumps_params={'ensure_ascii': False})  

def buscar_lanchonete(request,nome):
    """ caso a lanchonte exister retorna seus pratos"""
    resultado = ""
    if Lanchonete.objects.filter(nome=nome).exists():
        lanchonete = Lanchonete.objects.values(
            'nome',
            'endereco__estado',
            'endereco__cidade',
            'telefone').filter( nome = nome )
        lanchonete = list(lanchonete)
        pratos = list(Prato.objects.values("nome","preco").filter(lanchonete__nome = nome) )
        resultado = {"lanchonete" : lanchonete,"pratos":pratos}
    else:
        resultado = {"result":"Lanchonete não encontrada"}    
    return JsonResponse(resultado, safe=False, json_dumps_params={'ensure_ascii': False})




def person(request):
    return JsonResponse({"name":"marcelo","age":"26"})
