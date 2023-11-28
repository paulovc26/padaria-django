from django.shortcuts import render
from .models import Produto

def home(request):
    context={}
    return render(request, 'meusite/home.html',context)

def produtosList(request):
    produtos = Produto.objects. all
    return render(request, 'meusite/produtos.html', {'produtos': produtos})