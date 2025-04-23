'''
from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

# View para listar as pessoas
def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro/listar_pessoas.html', {'pessoas': pessoas})

# View para cadastrar uma pessoa
def cadastrar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'cadastro/cadastrar_pessoa.html', {'form': form})

# View para editar uma pessoa
def editar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'cadastro/editar_pessoa.html', {'form': form})

# View para deletar uma pessoa
def deletar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    pessoa.delete()
    return redirect('listar_pessoas')
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import Pessoa
from .forms import PessoaForm
from django.db.models import Q
from fpdf import FPDF
from datetime import datetime

# Página principal redireciona para cadastro
def home(request):
    return redirect('cadastrar_pessoa')

# Cadastrar ou editar pessoa
def cadastrar_pessoa(request, pk=None):
    if pk:
        pessoa = get_object_or_404(Pessoa, pk=pk)
    else:
        pessoa = None

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            try:
                form.save()
                return redirect('listar_pessoas')
            except Exception as e:
                form.add_error(None, f"Erro ao salvar: {e}")
    else:
        form = PessoaForm(instance=pessoa)

    return render(request, 'cadastro/cadastrar_pessoa.html', {'form': form, 'pessoa': pessoa})

# Autocomplete busca por nome (AJAX)
def buscar_pessoas(request):
    if 'term' in request.GET:
        qs = Pessoa.objects.filter(nome__icontains=request.GET.get('term'))
        nomes = list(qs.values('id', 'nome'))
        return JsonResponse(nomes, safe=False)
    return JsonResponse([], safe=False)

# Listar pessoas
def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro/listar_pessoas.html', {'pessoas': pessoas})

# Deletar com confirmação e exportação

def deletar_pessoa(request, pk):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == 'POST':
        response = gerar_pdf_usuario(pessoa)
        pessoa.delete()
        return response
    return render(request, 'cadastro/deletar_pessoa.html', {'pessoa': pessoa})

# Exportar um único usuário em PDF
def gerar_pdf_usuario(pessoa):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Dados de {pessoa.nome}", ln=True, align='C')
    for field in pessoa._meta.fields:
        valor = getattr(pessoa, field.name)
        pdf.cell(200, 10, txt=f"{field.verbose_name}: {valor}", ln=True)
    response = HttpResponse(pdf.output(dest='S').encode('latin1'))
    response['Content-Disposition'] = f'attachment; filename="pessoa_{pessoa.id}.pdf"'
    return response

# Exportar todas as pessoas em PDF (uma por página)
def exportar_pdf_todos(request):
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    for pessoa in Pessoa.objects.all():
        pdf.add_page()
        pdf.cell(200, 10, txt=f"Dados de {pessoa.nome}", ln=True, align='C')
        for field in pessoa._meta.fields:
            valor = getattr(pessoa, field.name)
            pdf.cell(200, 10, txt=f"{field.verbose_name}: {valor}", ln=True)
    response = HttpResponse(pdf.output(dest='S').encode('latin1'))
    response['Content-Disposition'] = 'attachment; filename="pessoas_completo.pdf"'
    return response

# Exportar por período com GET ?inicio=yyyy-mm-dd&fim=yyyy-mm-dd
def exportar_por_periodo(request):
    inicio = request.GET.get('inicio')
    fim = request.GET.get('fim')
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pessoas = Pessoa.objects.filter(data_registro__range=[inicio, fim])
    for pessoa in pessoas:
        pdf.add_page()
        pdf.cell(200, 10, txt=f"Dados de {pessoa.nome}", ln=True, align='C')
        for field in pessoa._meta.fields:
            valor = getattr(pessoa, field.name)
            pdf.cell(200, 10, txt=f"{field.verbose_name}: {valor}", ln=True)
    response = HttpResponse(pdf.output(dest='S').encode('latin1'))
    response['Content-Disposition'] = 'attachment; filename="pessoas_periodo.pdf"'
    return response
