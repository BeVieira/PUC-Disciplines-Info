from django.db import models

# Create your models here.
from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    site = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=100)
    dia_horario = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return f"{self.codigo} - {self.nome}"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Review(models.Model):
    nota = models.IntegerField()
    data = models.DateField()
    metodo_avaliacao = models.CharField(max_length=100)
    estilo_aula = models.CharField(max_length=100)
    presenca = models.BooleanField()
    dificuldade = models.CharField(max_length=100)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='reviews')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review de {self.aluno} para {self.disciplina}"
