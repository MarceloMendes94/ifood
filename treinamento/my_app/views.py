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

def buscar_estado(request,sigla):
    saida = ""
    if (len(sigla)==2):
        sigla=sigla.upper()
        saida = list(Lanchonete.objects.values(
            'nome',
            'endereco__estado',
            'endereco__cidade',
            'telefone').filter(
                endereco__estado  =  sigla) )

    return JsonResponse({"result":saida})

def buscar_estado_cidade(request,sigla,cidade):
    saida = ""
    if (len(sigla)==2):
        sigla=sigla.upper()
        saida = list(Lanchonete.objects.values(
            'nome',
            'endereco__estado',
            'endereco__cidade',
            'telefone').filter(
                endereco__estado  =  sigla,
                endereco__cidade  =  cidade) )

    return JsonResponse({"result":saida})

def buscar_max_preco(request,valor):
    saida = ""
    if(Prato.objects.filter( preco__lte = valor ).exists()):
        saida = list(
            Prato.objects.values(
                "nome",
                "preco",
                "lanchonete__nome",
                "lanchonete__telefone",
                "lanchonete__endereco__cidade",
                "lanchonete__endereco__estado",
                ).filter(
                    preco__lte = valor,
                )
            )

    return JsonResponse({"result":saida})

def buscar_estado_cidade_max_preco(request,sigla,cidade,valor):
    saida = ""
    if (len(sigla)==2 and sigla.isalpha()):
        if(Prato.objects.filter( preco__lte = valor,lanchonete__endereco__estado = sigla,lanchonete__endereco__cidade = cidade ).exists()):
            saida = list(
                Prato.objects.values(
                    "nome",
                    "preco",
                    "lanchonete__nome",
                    "lanchonete__telefone",
                    ).filter(
                        preco__lte = valor,
                        lanchonete__endereco__estado = sigla,
                        lanchonete__endereco__cidade = cidade ))

    return JsonResponse({"result":saida})