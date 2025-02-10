from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Realizar login do usuário
            login(request, user)
            return redirect('home')  # Redireciona para a página inicial, altere conforme necessário
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'login.html')  # Retorna o formulário de login

def menu(request):
    return render(request, 'menu.html')