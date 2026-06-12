from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Rol, Usuario, Ajuste
from .forms import RolForm, UsuarioForm, AjusteForm

# ==========================================
# AUTENTICACIÓN
# ==========================================

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('login')

# ==========================================
# DASHBOARD
# ==========================================

@login_required
def dashboard(request):
    total_roles = Rol.objects.count()
    total_usuarios = Usuario.objects.count()
    usuarios_activos = Usuario.objects.filter(estado=True).count()
    
    # Obtener configuración activa
    config = Ajuste.objects.first()
    paginacion = config.paginacion if config else 10
    
    # Elementos recientes para visualización en el dashboard
    recent_users = Usuario.objects.select_related('rol').order_by('-id')[:5]
    recent_roles = Rol.objects.order_by('-id')[:5]
    
    context = {
        'total_roles': total_roles,
        'total_usuarios': total_usuarios,
        'usuarios_activos': usuarios_activos,
        'paginacion_defecto': paginacion,
        'recent_users': recent_users,
        'recent_roles': recent_roles,
    }
    return render(request, 'dashboard.html', context)

# ==========================================
# CRUD DE ROLES
# ==========================================

@login_required
def roles_list(request):
    roles = Rol.objects.all()
    return render(request, 'roles/roles_list.html', {'roles': roles})

@login_required
def rol_create(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol creado exitosamente.')
            return redirect('roles')
        else:
            messages.error(request, 'Error al crear el rol. Verifica los datos.')
    else:
        form = RolForm()
    return render(request, 'roles/rol_form.html', {'form': form, 'action': 'Crear'})

@login_required
def rol_edit(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid():
            form.save()
            messages.success(request, 'Rol actualizado exitosamente.')
            return redirect('roles')
        else:
            messages.error(request, 'Error al actualizar el rol. Verifica los datos.')
    else:
        form = RolForm(instance=rol)
    return render(request, 'roles/rol_form.html', {'form': form, 'action': 'Editar', 'rol': rol})

@login_required
def rol_delete(request, pk):
    rol = get_object_or_404(Rol, pk=pk)
    # Control de Integridad referencial
    usuarios_con_rol = Usuario.objects.filter(rol=rol).count()
    
    if request.method == 'POST':
        if usuarios_con_rol > 0:
            messages.error(request, f'No se puede eliminar el rol "{rol.descripcion}" porque está asignado a {usuarios_con_rol} usuario(s).')
            return redirect('roles')
        rol.delete()
        messages.success(request, 'Rol eliminado exitosamente.')
        return redirect('roles')
        
    return render(request, 'roles/rol_confirm_delete.html', {
        'rol': rol,
        'usuarios_con_rol': usuarios_con_rol
    })

# ==========================================
# CRUD DE USUARIOS
# ==========================================

@login_required
def usuarios_list(request):
    usuarios = Usuario.objects.select_related('rol').all()
    return render(request, 'usuarios/usuarios_list.html', {'usuarios': usuarios})

@login_required
def usuario_create(request):
    if Rol.objects.count() == 0:
        messages.warning(request, 'Debes crear al menos un Rol antes de registrar un Usuario.')
        return redirect('roles')
        
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('usuarios')
        else:
            messages.error(request, 'Error al registrar el usuario. Verifica los datos.')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/usuario_form.html', {'form': form, 'action': 'Crear'})

@login_required
def usuario_edit(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('usuarios')
        else:
            messages.error(request, 'Error al actualizar el usuario. Verifica los datos.')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/usuario_form.html', {'form': form, 'action': 'Editar', 'usuario': usuario})

@login_required
def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente.')
        return redirect('usuarios')
    return render(request, 'usuarios/usuario_confirm_delete.html', {'usuario': usuario})

# ==========================================
# CRUD DE AJUSTES
# ==========================================

@login_required
def ajustes_list(request):
    ajustes = Ajuste.objects.all()
    return render(request, 'ajustes/ajustes_list.html', {'ajustes': ajustes})

@login_required
def ajuste_create(request):
    if request.method == 'POST':
        form = AjusteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ajuste global registrado.')
            return redirect('ajustes')
        else:
            messages.error(request, 'Error al registrar el ajuste. Verifica los datos.')
    else:
        form = AjusteForm()
    return render(request, 'ajustes/ajuste_form.html', {'form': form, 'action': 'Crear'})

@login_required
def ajuste_edit(request, pk):
    ajuste = get_object_or_404(Ajuste, pk=pk)
    if request.method == 'POST':
        form = AjusteForm(request.POST, instance=ajuste)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ajuste global actualizado.')
            return redirect('ajustes')
        else:
            messages.error(request, 'Error al actualizar el ajuste. Verifica los datos.')
    else:
        form = AjusteForm(instance=ajuste)
    return render(request, 'ajustes/ajuste_form.html', {'form': form, 'action': 'Editar', 'ajuste': ajuste})

@login_required
def ajuste_delete(request, pk):
    ajuste = get_object_or_404(Ajuste, pk=pk)
    total_ajustes = Ajuste.objects.count()
    
    if request.method == 'POST':
        if total_ajustes <= 1:
            messages.error(request, 'No puedes eliminar la única configuración del sistema. Debe haber al menos una.')
            return redirect('ajustes')
        ajuste.delete()
        messages.success(request, 'Ajuste eliminado exitosamente.')
        return redirect('ajustes')
        
    return render(request, 'ajustes/ajuste_confirm_delete.html', {
        'ajuste': ajuste,
        'total_ajustes': total_ajustes
    })