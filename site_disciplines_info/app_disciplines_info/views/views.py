from django.shortcuts import render
from app_disciplines_info.models import Disciplina, Professor

def consultar_view(request):
    if request.method == 'POST':
        consulta = None
        resultado = {}
        codigo = request.POST.get('codigo')
        nome = request.POST.get('nome')
        professor = request.POST.get('professor')
        dia = request.POST.get('dia')
        horario = request.POST.get('horario')

        if codigo:
            consulta = Disciplina.objects.filter(codigo__icontains=codigo)
        else:
            if nome:
                consulta = Disciplina.objects.filter(nome__icontains=nome)  
            else:
                consulta = Disciplina.objects.filter(professor__nome__icontains=professor)
        
        if dia:
            consulta = consulta.filter(dia__icontains=dia)
        
        if horario:
            consulta = consulta.filter(horario__icontains=horario)

        for disciplina in consulta:
            chave = (disciplina.codigo, disciplina.nome, disciplina.professor.nome)
            if chave not in resultado:
                resultado[chave] = []
            resultado[chave].append(f'{disciplina.dia} / {disciplina.horario}')

        return render(request, 'consulta.html', {'resultado': resultado})
    
    return render(request, 'consulta.html')

def disciplina_view(request):
    codigo = request.GET.get('codigo')
    horario = request.GET.get('horario')
    disciplina = Disciplina.objects.filter(codigo__icontais=codigo)
    disciplina = disciplina.filter(horario__icontais=horario)


    return render(request, 'disciplina.html', {'disciplina': disciplina})