from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse

from registros.models import RegistroAgua, RegistroBloqueador, RegistroRopa
from .models import PerfilUsuario
from registros.forms import RegistroAguaForm, RegistroRopaForm, RegistroBloqueadorForm
from .forms import PerfilUsuarioForm, RegistroUsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.

@login_required
def home(request):
    data = {'form_agua': RegistroAguaForm, 'form_ropa': RegistroRopaForm, 'form_bloqueador': RegistroBloqueadorForm}

    if request.method == "POST":
        form_agua = RegistroAguaForm(request.POST, user=request.user)
        if form_agua.is_valid():
            agua_instance = form_agua.save()
            messages.success(request, "Registro de agua guardado correctamente")
            data['form_agua'] = RegistroAguaForm()
        else:
            data['form_agua'] = form_agua

        form_ropa = RegistroRopaForm(request.POST, user=request.user)
        if form_ropa.is_valid():
            ropa_instance = form_ropa.save()
            messages.success(request, "Registro de ropa guardado correctamente")
            data['form_ropa'] = RegistroRopaForm()
        else:
            data['form_ropa'] = form_ropa

        form_bloqueador = RegistroBloqueadorForm(request.POST, user=request.user)
        if form_bloqueador.is_valid():
            bloqueador_instance = form_bloqueador.save()
            messages.success(request, "Registro de bloqueador guardado correctamente")
            data['form_bloqueador'] = RegistroBloqueadorForm()
        else:
            data['form_bloqueador'] = form_bloqueador
    return render(request, 'home.html', data)

def registro(request):
    data = {'form':RegistroUsuarioForm}
    if request.method == "POST":
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data['form'] = formulario
    return render(request, 'registration/registro.html', data)

def olvidar_contrasena(request):
    return render(request, 'olvidar_contrasena.html')

def mas_opciones(request):
    return render(request, 'mas_opciones.html')

@login_required
def perfil(request):
    data = {'form': PerfilUsuarioForm}

    user = request.user
    agua_registros = user.perfil_usuario.registroagua_set.all()
    ropa_registros = user.perfil_usuario.registroropa_set.all()
    bloqueador_registros = user.perfil_usuario.registrobloqueador_set.all()

    if request.method == 'POST':
        formulario = PerfilUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "datos guardados"
        else:
            data['form'] = formulario
    data['agua_registros'] = agua_registros
    data['ropa_registros'] = ropa_registros
    data['bloqueador_registros'] = bloqueador_registros
    return render(request, 'perfil.html', data)

# class PerfilView(View):
#     template_name = 'usuarios/perfil.html'

#     @method_decorator(login_required)
#     def get(self, request, *args, **kwargs):
#         if hasattr(request.user, 'perfilusuario'):
#             form = PerfilUsuarioForm(instance=request.user.perfilusuario)
#         else:
#             form = PerfilUsuarioForm()

#         return render(request, self.template_name, {'form': form})

#     @method_decorator(login_required)
#     def post(self, request, *args, **kwargs):
#         if hasattr(request.user, 'perfilusuario'):
#             form = PerfilUsuarioForm(request.POST, instance=request.user.perfilusuario)
#         else:
#             form = PerfilUsuarioForm(request.POST)

#         if form.is_valid():
#             perfil_usuario = form.save(commit=False)
#             perfil_usuario.usuario = request.user
#             perfil_usuario.save()
#             return redirect('perfil')
        
#         return render(request, self.template_name, {'form': form})

def test(request):
    return render(request, 'test.html')