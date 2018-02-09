from django.shortcuts import render, HttpResponse


def paginainicial(request):
    return HttpResponse("Bem vindo a pagina do app de contas")

def login(request):
    return HttpResponse("Pagina de login")
