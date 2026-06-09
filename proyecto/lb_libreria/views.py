from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.cache import cache_control
from django.views.decorators.cache import never_cache


def auth_render(request, template_name):
    if not request.user.is_authenticated:
        return redirect('home')
    return render(request, template_name)

@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def home_view(request):
    return render(request, 'index.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def logout_view(request):
    logout(request)
    response = redirect('home')
    response.delete_cookie(settings.SESSION_COOKIE_NAME)
    return response


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def usuario_view(request):
    return auth_render(request, 'usuario.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def personas_view(request):
    return auth_render(request, 'personas.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def metodos_pago_view(request):
    return auth_render(request, 'metodos_pago.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def categorias_view(request):
    return auth_render(request, 'categorias.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def marcas_view(request):
    return auth_render(request, 'marcas.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def proveedores_view(request):
    return auth_render(request, 'proveedores.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def productos_view(request):
    return auth_render(request, 'productos.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def pedidos_view(request):
    return auth_render(request, 'pedidos.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def pagos_view(request):
    return auth_render(request, 'pagos.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def permisos_view(request):
    return auth_render(request, 'permisos.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def detalle_permisos_view(request):
    return auth_render(request, 'detalle_permisos.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def roles_view(request):
    return auth_render(request, 'roles.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def detalle_roles_view(request):
    return auth_render(request, 'detalle_roles.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def configuracion_view(request):
    return auth_render(request, 'configuracion.html')


@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
def validar_usuario(request):
    if request.method == 'POST':
        v_usuario = request.POST.get('usuario')
        v_contrasena = request.POST.get('contrasena')

        user = authenticate(request, username=v_usuario, password=v_contrasena)

        if user is not None:
            login(request, user)
            request.session['usuario_id'] = user.id

            return JsonResponse({
                'success': True,
                'redirect_url': '/inicio_panel/'
            })
        else:
            return JsonResponse({
                'success': False,
                'mensaje': 'Credenciales incorrectas'
            })

    return render(request, 'index.html')

@never_cache
@cache_control(no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url='/inicio/')
def dashboard_view(request):
    return auth_render(request, 'dashboard.html')
