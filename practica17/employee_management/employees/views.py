from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Vista para la página de inicio
def home(request):
    return render(request, 'employees/home.html')

# Vista para el registro de usuarios
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        if password != password_confirmation:
            return render(request, 'employees/register.html', {
                'error': 'Las contraseñas no coinciden.'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'employees/register.html', {
                'error': 'El nombre de usuario ya existe.'
            })

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    return render(request, 'employees/register.html')

# Vista para el inicio de sesión
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'employees/login.html', {
                'error': 'Nombre de usuario o contraseña incorrectos.'
            })

    return render(request, 'employees/login.html')

# Vista para cerrar sesión
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

# Vista para mostrar el perfil del usuario
@login_required
def profile(request):
    return render(request, 'employees/profile.html')

# Vista para mostrar todos los perfiles en un formato de cuadro
@login_required
def profile_list(request):
    users = User.objects.all()
    return render(request, 'employees/profile_list.html', {'users': users})

# Vista para editar un perfil de usuario
@login_required
def profile_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile_list')
    return render(request, 'employees/profile_edit.html', {'user': user})

# Vista para eliminar un perfil de usuario
@login_required
def profile_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('profile_list')
    return render(request, 'employees/profile_delete.html', {'user': user})
