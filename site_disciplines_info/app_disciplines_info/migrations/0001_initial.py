# Generated by Django 5.1.1 on 2024-10-11 23:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvaliacaoTipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nome', models.CharField(max_length=100)),
                ('dia', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='disciplinas', to='app_disciplines_info.professor')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=100)),
                ('dificuldade', models.FloatField()),
                ('criadoEm', models.DateField()),
                ('estilo_aula', models.CharField(max_length=100)),
                ('presenca', models.BooleanField()),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='app_disciplines_info.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='QtdAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_disciplines_info.avaliacaotipo')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='app_disciplines_info.review')),
            ],
        ),
    ]
