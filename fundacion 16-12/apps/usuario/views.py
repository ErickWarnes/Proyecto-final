# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, DeleteView
# from .models import Usuario
# from .forms import RegistroUsuarioForm,UserCreationForm
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import User

# User = get_user_model()

# class RegistrarUsuario(CreateView):
#     model         = User
#     form_class    = RegistroUsuarioForm
#     template_name = 'registration/registro.html'
#     success_url   = reverse_lazy('apps.usuario:login')

# def Usuarios(request):
#     usuarios = Usuario.objects.all()
#     context={
#         'usuarios': usuarios,
#     }
#     return render(request,'usuario/listarUsuarios.html', context)

# # class DeleteUsuario(DeleteView):
# #     model           = Usuario
# #     template_name = 'usuario/usuario_delete.html'
# #     success_url   = reverse_lazy('apps.usuario:listarUsuarios')


from django.shortcuts import render,redirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, DeleteView
from django.contrib import messages
# from .forms import Usuario
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " La Cuenta se creo con Exito")
            return redirect('login')
    context = {'form':form}
    return render(request,'registration/register.html',context)

def loginPage(request):
    
    if request.method == 'POST':
        
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        # nombre_usuario = form.cleaned_data.get('username')
        # contra = form.cleaned_data.get('password')

        user = authenticate(request, username=username1,password=password1)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
         messages.info(request, 'Usuario o contraseña es incorrecto')   
    context = {}
    return render(request,'registration/login.html',context)

# def logoutUser(request):
#     logout(request)
#     return redirect('/')

# class RegistrarUsuario(CreateView):
#     model         = Usuario
#     form_class    = RegistroUsuarioForm
#     template_name = 'log/register.html'
#     success_url   = reverse_lazy('App.usuario:login')

# def Usuarios(request):
#     usuarios = Usuario.objects.all()
#     context={
#         'usuarios': usuarios,
#     }
#     return render(request,'usuario/listarUsuarios.html', context)

# class DeleteUsuario(DeleteView):
#     model           = Usuario
#     template_name = 'usuario/usuario_delete.html'
#     success_url   = reverse_lazy('App.usuario:listarUsuarios')