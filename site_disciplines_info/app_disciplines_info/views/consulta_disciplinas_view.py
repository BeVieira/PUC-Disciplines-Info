from django.shortcuts import render
from app_disciplines_info.models import Disciplina

def consulta_disciplina(request):
    resultado = None
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nome = request.POST.get('nome')

        # Consultar disciplina pelo código
        if codigo:
            resultado = Disciplina.objects.filter(codigo__iexact=codigo).first()
        
        # Se não encontrar pelo código, tenta buscar pelo nome
        if not resultado and nome:
            resultado = Disciplina.objects.filter(nome__icontains=nome).first()

    return resultado

