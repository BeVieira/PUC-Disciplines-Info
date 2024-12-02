from django.shortcuts import render
from datetime import datetime
from app_disciplines_info.models import Disciplina, Professor, Review

def consultar_view(request):
    if request.method == 'POST':
        consulta = None
        resultado = {}
        codigo = request.POST.get('codigo')
        nome = request.POST.get('nome')
        professor = request.POST.get('professor')
        dia = request.POST.get('dia')
        horario = request.POST.get('horario')
        filtros = {}

        if codigo:
            filtros["codigo__icontains"] = codigo
        if nome:
            filtros["nome__icontains"] = nome
        if professor:
            filtros["professor__nome__icontains"] = professor
        if dia:
            filtros["dia__icontains"] = dia
        if horario:
            filtros["horario__icontains"] = horario

        consulta = Disciplina.objects.filter(**filtros)

        if not (codigo or nome or professor or dia or horario):
            consulta = Disciplina.objects.all()

        for disciplina in consulta:
            chave = (disciplina.codigo, disciplina.nome, disciplina.professor.nome)
            if chave not in resultado:
                resultado[chave] = []
            resultado[chave].append(f'{disciplina.dia} / {disciplina.horario}')

        return render(request, 'consulta.html', {'resultado': resultado})
    
    return render(request, 'consulta.html', {'resultado': None})

def disciplina_view(request, codigo, professor):
    disciplina = Disciplina.objects.filter(codigo=codigo)
    disciplina = disciplina.filter(professor__nome=professor)
    horarios = disciplina.values_list('horario', flat=True) 
    dias = disciplina.values_list('dia', flat=True)
    media = disciplina.calcular_media()
    listaHorarios =[]

    for i in range(len(horarios)):
        listaHorarios.append(f'{dias[i]} / {horarios[i]}')

    objetoTela = {
        'codigo': disciplina[0].codigo,
        'nome': disciplina[0].nome,
        'professor': disciplina[0].professor.nome,
        'horarios' : listaHorarios,
        'ementa': disciplina[0].ementa,
        'media': media
    }

    return render(request, 'disciplina.html', objetoTela)

def salvar_feedback_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        experiencia = request.POST.get('experiencia')
        nota = float(request.POST.get('nota'))

        Review.objects.create(
            autor=nome,
            experiencia=experiencia,
            dificuldade=nota,
            criadoEm = datetime.now()
        )
        return