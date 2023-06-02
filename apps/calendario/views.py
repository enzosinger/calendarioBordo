from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.calendario.models import Calendario
from apps.calendario.forms import CalendarioForms
from apps.usuarios.models import Usuario


def index(request):
    selected_day = request.GET.get('day')
    if  not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para fazer isso.')
        return redirect('login')
    current_user = request.user
    id = current_user.id
    perfil = get_object_or_404(Usuario, pk=id)
    calendario = Calendario.objects.filter(data__day=1)
    dia = 24

    calendar = [
    ['26', '27', '28', '29', '30', '31', '01'],
    ['02', '03', '04', '05', '06', '07', '08'],
    ['09', '10', '11', '12', '13', '14', '15'],
    ['16', '17', '18', '19', '20', '21', '22'],
    ['23', '24', '25', '26', '27', '28', '29'],
    ['30', '01', '02', '03', '04', '05', '06',],
]

    context = {
        'calendar': calendar
    }
    return render(request, 'calendario.html',{"cards": calendario, "context": context, "dia": dia, "id": perfil})

def calendario(request, dia):
    if  not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para fazer isso.')
        return redirect('login')
    current_user = request.user
    id = current_user.id
    perfil = get_object_or_404(Usuario, pk=id)
    calendario = Calendario.objects.all

    calendar = [
    ['26', '27', '28', '29', '30', '31', '01'],
    ['02', '03', '04', '05', '06', '07', '08'],
    ['09', '10', '11', '12', '13', '14', '15'],
    ['16', '17', '18', '19', '20', '21', '22'],
    ['23', '24', '25', '26', '27', '28', '29'],
    ['30', '01', '02', '03', '04', '05', '06',],
    ]

    busca = Calendario.objects.filter(data__day=dia)

    context = {
        'calendar': calendar
    }
    return render(request, 'calendario.html',{"cards": busca, "context": context, "dia": dia, "id": perfil})

def cadastro_eventos(request):
    if  not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para fazer isso.')
        return redirect('login')
    if  not request.user.is_moderator:
        messages.error(request, 'Você não tem permissão para ver essa página.')
        return redirect('login')
    form = CalendarioForms
    if request.method == 'POST':
        form = CalendarioForms(request.POST)

        if form.is_valid():
            nome = form['nome'].value()
            descricao = form['descricao'].value()
            disciplina = form['disciplina'].value()
            data = form['data'].value()
            evento = Calendario.objects.create(
                nome = nome,
                descricao = descricao,
                disciplina = disciplina,
                data = data
            )
            evento.save()
            messages.success(request, f"Cadastro efetuado com sucesso!")
            return redirect('cadastro_eventos')
    return render(request, 'cadastro_eventos.html', {"form": form})