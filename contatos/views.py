from django.shortcuts import render, redirect, get_object_or_404
from .models import Contatos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import openai


@login_required(redirect_field_name='login')
def index(request):
    contatos = Contatos.objects.filter(
        usuario_id=request.user.id).order_by('-id')
    return render(request, 'pages/index.html', {'contatos': contatos})


@login_required(redirect_field_name='login')
def ver_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'pages/ver_usuarios.html', {'usuarios': usuarios})


@login_required(redirect_field_name='login')
def ver_contatos(request, id):
    contatos = Contatos.objects.filter(usuario_id=id).order_by('-id')
    return render(request, 'pages/ver_contatos.html', {'contatos': contatos})


def search(request):
    q = request.GET.get('search')
    contatos = Contatos.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'contatos': contatos})


def detalhes(request, id):
    # contato = Contatos.objects.get(id=id)
    contato = get_object_or_404(Contatos, id=id)
    return render(request, 'pages/detalhes.html', {'contato': contato})


def deletar(request, id):
    contato = Contatos.objects.get(id=id)
    # refazer = contato
    contato.delete()
    return redirect('home')


def criar_descricao(nome):
    API_KEY = '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'
    openai.api_key = API_KEY
    modelo = 'text-davinci-003'
    pergunta = f'Gere uma profissão para uma pessoa de nome {nome}'
    response = openai.Completion.create(
        engine=modelo,
        prompt=pergunta,
        max_tokens=1024
    )
    return (response.choices[0]['text'])


def adicionar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        if descricao == '':
            descricao = criar_descricao(nome)
        data_nascimento = request.POST.get('data_nascimento')
        imagem = request.FILES.get('imagem')

        novo_contato = Contatos(usuario_id=request.user.id, nome=nome, cpf=cpf, email=email, telefone=telefone, altura=altura,
                                descricao=descricao, data_nascimento=data_nascimento, imagem=imagem, ativo=True)

        novo_contato.save()

        return redirect('home')

    else:
        return render(request, 'pages/adicionar.html')


def editar(request, id):
    contato = Contatos.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        data_nascimento = request.POST.get('data_nascimento')
        ativo = request.POST.get('ativo')
        if ativo == None:
            ativo = False
        else:
            ativo = True
        imagem = request.FILES.get('imagem')
        print(imagem)

        contato.nome = nome
        contato.cpf = cpf
        contato.email = email
        contato.telefone = telefone
        contato.altura = altura
        contato.descricao = descricao
        contato.data_nascimento = data_nascimento
        contato.ativo = ativo
        if imagem != None:
            contato.imagem = imagem

        contato.save()

        return redirect('home')

    else:
        return render(request, 'pages/editar.html', {'contato': contato})
