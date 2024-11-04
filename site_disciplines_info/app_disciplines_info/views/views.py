from django.shortcuts import render
from app_disciplines_info.models import Disciplina, Professor

def consultar_view(request):
    if request.method == 'POST':
        consulta = None
        resultado = {}
        codigo = request.POST.get('codigo')
        nome = request.POST.get('nome')
        professor = request.POST.get('professor')

        if codigo:
            consulta = Disciplina.objects.filter(codigo=codigo)
        else:
            if nome:
                consulta = Disciplina.objects.filter(nome__icontains=nome)  
            else:
                consulta = Disciplina.objects.filter(professor__nome__icontains=professor)

        for disciplina in consulta:
            chave = (disciplina.codigo, disciplina.nome, disciplina.professor.nome)
            if chave not in resultado:
                resultado[chave] = []
            resultado[chave].append(f'{disciplina.dia} / {disciplina.horario}')

        return render(request, 'consulta.html', {'resultado': resultado})
    
    return render(request, 'consulta.html')

