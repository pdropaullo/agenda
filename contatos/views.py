from django.shortcuts import render
from .models import Contatos


def index(request):
    contatos = Contatos.objects.all()
    return render(request, 'pages/index.html', {'contatos': contatos})


def search(request):
    q = request.GET.get('search')
    contatos = Contatos.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'contatos': contatos})
