from django.shortcuts import render
from .models import Registro

def home(request):
    return render(request,'app/index.html')

def agendamentos(request):
    return render(request,'app/agendamentos.html')

def registros(request):
    novo_agendamento = Registro()
    novo_agendamento.nome = request.POST.get('nome')
    novo_agendamento.endereco = request.POST.get('endereco')
    novo_agendamento.email = request.POST.get('email')
    novo_agendamento.telefone = request.POST.get('telefone')
    novo_agendamento.data_coleta = request.POST.get('data_coleta')
    novo_agendamento.hora_coleta = request.POST.get('hora_coleta')

    novo_agendamento.save()

    agendamentos = {
        'agendamentos':Registro.objects.all()
    }

    return render(request,'app/registros.html',agendamentos)