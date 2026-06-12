from .models import Ajuste

def global_settings(request):
    ajuste = Ajuste.objects.first()
    if not ajuste:
        ajuste = Ajuste.objects.create(
            nombre_aplicacion="Sistema de Gestión",
            estado_sitio=True,
            paginacion=10,
            logs_mantenimiento="Sistema inicializado"
        )
    
    active_page = ''
    if request.resolver_match:
        active_page = request.resolver_match.url_name
    else:
        path = request.path
        if 'roles' in path:
            active_page = 'roles'
        elif 'usuarios' in path:
            active_page = 'usuarios'
        elif 'ajustes' in path:
            active_page = 'ajustes'
        elif 'dashboard' in path:
            active_page = 'dashboard'
            
    return {
        'global_ajustes': ajuste,
        'active_page': active_page
    }
