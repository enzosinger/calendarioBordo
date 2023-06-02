from django.shortcuts import get_object_or_404, render, redirect

from apps.usuarios.forms import LoginForms, CadastroForms, EditarForms

from apps.usuarios.models import Usuario

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages

def login(request):
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
            else:
                messages.error(request, 'Email e/ou senha inválidos.')
                return redirect('login')
    else:
        form = LoginForms()
        return render(request, 'login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha'].value()
            if Usuario.objects.filter(username = nome).exists() or Usuario.objects.filter(email = email).exists():
                messages.error(request, 'Email ou usuário ja cadastrado.')
                return redirect('cadastro')
            
            usuario = Usuario.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )
            usuario.save()
            messages.success(request, f"Cadastro efetuado com sucesso!")
            return redirect('login')
    return render(request, 'cadastro.html', {"form": form})

def perfil(request):
    if  not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para fazer isso.')
        return redirect('login')
    current_user = request.user
    id = current_user.id
    perfil = get_object_or_404(Usuario, pk=id)
    return render(request, 'perfil.html', {'id': perfil})

def editar_perfil(request):
    if  not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para fazer isso.')
        return redirect('login')
    current_user = request.user
    id = current_user.id
    perfil = get_object_or_404(Usuario, pk=id)
    form = EditarForms(instance = perfil)
    if request.method == 'POST':
        form = EditarForms(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil editado com sucesso!')
            return redirect('perfil')
    return render(request, 'editar_perfil.html', {'form': form, 'id': perfil})

def logout(request):
    if  not request.user.is_authenticated:
        messages.error(request, 'Você já esta deslogado.')
        return redirect('login')
    auth.logout(request)
    messages.success(request,'Deslogado com sucesso!')
    return redirect('login')

def apagar_conta(request):
    if  not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para fazer isso.')
        return redirect('login')
    current_user = request.user
    id = current_user.id
    perfil = get_object_or_404(Usuario, pk=id)
    perfil.delete()
    messages.success(request, 'Conta excluída com sucesso.')
    return redirect('cadastro')
