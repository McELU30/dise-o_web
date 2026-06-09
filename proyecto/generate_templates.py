from pathlib import Path

base = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-store, no-cache, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" />
    <title>{% block title %}MultiBlas{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        :root {
            color-scheme: dark;
            --bg: #090b12;
            --card: #111827;
            --card-border: rgba(255,255,255,0.08);
            --text: #e5e7eb;
            --muted: #9ca3af;
            --accent: #4f46e5;
            --accent-soft: rgba(79,70,229,0.12);
        }
        html, body {
            min-height: 100%;
            background: radial-gradient(circle at top left, rgba(79,70,229,0.12), transparent 35%),
                        linear-gradient(180deg, #0b0f19 0%, #090b12 100%);
            color: var(--text);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        body { margin: 0; }
        .page-header {
            padding: 2rem 0 1.5rem;
        }
        .page-title {
            font-size: clamp(1.8rem, 2.2vw, 2.6rem);
            letter-spacing: 0.08em;
        }
        .page-badge {
            border-radius: 999px;
            font-size: 0.8rem;
            padding: 0.45rem 0.9rem;
            background: rgba(79,70,229,0.12);
            color: #c7d2fe;
        }
        .nav-panel {
            border-bottom: 1px solid rgba(255,255,255,0.06);
            background: rgba(16,24,40,0.95);
            backdrop-filter: blur(12px);
        }
        .nav-link.custom {
            color: var(--muted);
            transition: color .2s ease, transform .15s ease;
        }
        .nav-link.custom:hover, .nav-link.custom.active {
            color: #fff;
            transform: translateY(-1px);
        }
        .card-surface {
            background: linear-gradient(180deg, rgba(15,23,42,0.95), rgba(17,24,39,0.95));
            border: 1px solid var(--card-border);
            border-radius: 1rem;
            box-shadow: 0 24px 80px rgba(0,0,0,0.15);
        }
        .card-surface .card-body { padding: 1.75rem; }
        .info-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.55rem 0.95rem;
            background: rgba(255,255,255,0.05);
            border-radius: 999px;
            border: 1px solid rgba(255,255,255,0.08);
            color: var(--text);
            font-size: 0.95rem;
        }
        .search-control {
            max-width: 360px;
            background: #0f1720;
            border: 1px solid rgba(255,255,255,0.08);
            color: var(--text);
        }
        .search-control:focus {
            outline: none;
            box-shadow: 0 0 0 0.25rem rgba(79,70,229,0.14);
        }
        .table-responsive {
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 1rem;
            overflow: hidden;
        }
        .table thead {
            background: rgba(255,255,255,0.04);
        }
        .table tbody tr:hover {
            background: rgba(255,255,255,0.04);
        }
        .status-chip {
            padding: 0.45rem 0.75rem;
            border-radius: 999px;
            font-size: 0.8rem;
            font-weight: 700;
        }
        .status-active { background: rgba(34,197,94,0.14); color: #a7f3d0; }
        .status-pending { background: rgba(245,158,11,0.16); color: #fbbf24; }
        .status-blocked { background: rgba(248,113,113,0.16); color: #fecaca; }
        .action-button {
            min-width: 140px;
            border-radius: 999px;
            transition: transform .2s ease, box-shadow .2s ease;
        }
        .action-button:hover {
            transform: translateY(-1px);
            box-shadow: 0 16px 32px rgba(79,70,229,0.12);
        }
        .chart-placeholder {
            min-height: 260px;
            border-radius: 1rem;
            background: linear-gradient(180deg, rgba(79,70,229,0.16), rgba(15,23,42,0.9));
            border: 1px solid rgba(255,255,255,0.08);
        }
        .highlight-box {
            background: rgba(79,70,229,0.12);
            border: 1px solid rgba(79,70,229,0.22);
            border-radius: 1rem;
            padding: 1.15rem 1.25rem;
        }
        .footer-note {
            color: var(--muted);
            font-size: 0.92rem;
        }
        @media (max-width: 991.98px) {
            .page-header { padding-top: 1.5rem; }
        }
    </style>
    {% block head %}{% endblock %}
</head>
<body>
    <header class="nav-panel py-3">
        <div class="container-fluid">
            <div class="d-flex flex-wrap align-items-center justify-content-between gap-3">
                <a href="{% url 'dashboard' %}" class="d-flex align-items-center text-decoration-none text-white fw-bold fs-5">
                    <i class="bi bi-cpu-fill fs-4 me-2 text-info"></i>MultiBlas
                </a>
                <div class="d-flex flex-wrap align-items-center gap-2">
                    <a href="{% url 'dashboard' %}" class="nav-link custom px-3 py-2">Dashboard</a>
                    <a href="{% url 'usuario' %}" class="nav-link custom px-3 py-2">Usuario</a>
                    <a href="{% url 'personas' %}" class="nav-link custom px-3 py-2">Personas</a>
                    <a href="{% url 'logout' %}" class="btn btn-sm btn-outline-light action-button">Cerrar sesión</a>
                </div>
                <div class="text-end text-muted small">
                    <div>Conectado como</div>
                    <strong>{{ user.username|default:"Administrador" }}</strong>
                </div>
            </div>
        </div>
    </header>

    <main class="container-xxl py-4">
        {% block content %}{% endblock %}
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmxc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    <script>
        window.addEventListener('pageshow', function(event) {
            if (event.persisted || (performance && performance.getEntriesByType && performance.getEntriesByType('navigation')[0]?.type === 'back_forward')) {
                window.location.reload();
            }
        });

        function filterTable(inputId, tableId) {
            const query = document.getElementById(inputId)?.value.toLowerCase().trim();
            const rows = document.querySelectorAll(`#${tableId} tbody tr`);
            if (!rows) return;
            rows.forEach(row => {
                const text = row.textContent.toLowerCase();
                row.style.display = text.includes(query) ? '' : 'none';
            });
        }

        function updateCounters() {
            document.querySelectorAll('[data-count]').forEach(el => {
                const value = el.getAttribute('data-count');
                el.textContent = value;
            });
        }

        document.addEventListener('DOMContentLoaded', () => {
            updateCounters();
        });
    </script>
    {% block scripts %}{% endblock %}
</body>
</html>
'''

login = '''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-store, no-cache, must-revalidate" />
    <meta http-equiv="Pragma" content="no-cache" />
    <meta http-equiv="Expires" content="0" />
    <title>Acceso MultiBlas</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <style>
        body {
            min-height: 100vh;
            background: linear-gradient(135deg, #0f1720 0%, #111827 45%, #0f1720 100%);
            color: #e5e7eb;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .auth-card {
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 1.35rem;
            background: rgba(15,23,42,0.95);
            box-shadow: 0 40px 80px rgba(0,0,0,0.22);
        }
        .brand-panel {
            min-height: 100vh;
            background: radial-gradient(circle at top left, rgba(59,130,246,0.28), transparent 40%),
                        url('https://images.unsplash.com/photo-1518770660439-4636190af475?ixlib=rb-4.0.3&auto=format&fit=crop&w=1400&q=80') no-repeat center/cover;
        }
        .brand-panel::before {
            content: '';
            position: absolute;
            inset: 0;
            background: rgba(15,23,42,0.65);
            border-radius: 1.35rem;
        }
        .brand-panel > * { position: relative; z-index: 1; }
        .brand-panel h1 {
            letter-spacing: 0.16em;
        }
        .form-control,
        .form-control:focus {
            border-radius: 0.85rem;
            background: rgba(15,23,42,0.9);
            border: 1px solid rgba(255,255,255,0.1);
            color: #e5e7eb;
            box-shadow: none;
        }
        .form-label { color: #cbd5e1; }
        .btn-login {
            border-radius: 999px;
            padding: 0.9rem 1.5rem;
            font-weight: 700;
        }
        .toggle-password {
            cursor: pointer;
            right: 1rem;
            top: 50%;
            transform: translateY(-50%);
            position: absolute;
            color: #94a3b8;
        }
        .form-note {
            color: #94a3b8;
            font-size: 0.95rem;
        }
        .panel-overlay {
            border-radius: 1.35rem;
            overflow: hidden;
        }
        .message-box {
            min-height: 58px;
        }
    </style>
</head>
<body>
    <div class="container-fluid min-vh-100">
        <div class="row g-0 min-vh-100">
            <div class="col-12 col-lg-6 d-flex align-items-center justify-content-center p-4 panel-overlay brand-panel text-white">
                <div class="text-center px-4 py-5">
                    <i class="bi bi-cpu-fill fs-1 text-info"></i>
                    <h1 class="display-5 fw-bold mt-4">MultiBlas</h1>
                    <p class="lead text-white-50 mt-3">Control moderno, navegación fluida y acceso seguro para tu sistema empresarial.</p>
                </div>
            </div>
            <div class="col-12 col-lg-6 d-flex align-items-center justify-content-center p-4">
                <div class="w-100" style="max-width: 480px;">
                    <div class="auth-card p-4 p-sm-5">
                        <div class="mb-4 text-center">
                            <div class="badge bg-info bg-opacity-10 text-info mb-3">Inicio de sesión</div>
                            <h2 class="fw-bold">Bienvenido de nuevo</h2>
                            <p class="form-note mb-0">Introduce tus credenciales para entrar al panel administrativo.</p>
                        </div>
                        <div id="mensaje-error" class="message-box"></div>
                        <form id="formLogin" method="POST" action="{% url 'validar_usuario' %}">
                            {% csrf_token %}
                            <div class="mb-3 form-floating">
                                <input type="text" class="form-control" id="usuarioInput" name="usuario" placeholder="Usuario" required>
                                <label for="usuarioInput">Usuario</label>
                            </div>
                            <div class="mb-4 form-floating position-relative">
                                <input type="password" class="form-control" id="contrasenaInput" name="contrasena" placeholder="Contraseña" required>
                                <label for="contrasenaInput">Contraseña</label>
                                <i class="bi bi-eye-slash toggle-password" id="iconoOjo" aria-label="Mostrar contraseña"></i>
                            </div>
                            <div class="d-flex justify-content-between align-items-center mb-4">
                                <div class="form-check">
                                    <input class="form-check-input" type="checkbox" id="recordarSesion">
                                    <label class="form-check-label form-note" for="recordarSesion">Recordar mi sesión</label>
                                </div>
                                <a href="#" class="form-note text-decoration-none">¿Olvidaste tu contraseña?</a>
                            </div>
                            <button type="submit" class="btn btn-primary btn-login w-100" id="btnSubmit">
                                <span id="textoBtn">Entrar al sistema</span>
                                <span class="spinner-border spinner-border-sm d-none ms-2" id="spinnerBtn" role="status" aria-hidden="true"></span>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script>
        const iconoOjo = document.getElementById('iconoOjo');
        const contrasenaInput = document.getElementById('contrasenaInput');
        const btnSubmit = document.getElementById('btnSubmit');
        const textoBtn = document.getElementById('textoBtn');
        const spinnerBtn = document.getElementById('spinnerBtn');
        const mensajeError = document.getElementById('mensaje-error');

        iconoOjo.addEventListener('click', () => {
            const visible = contrasenaInput.type === 'text';
            contrasenaInput.type = visible ? 'password' : 'text';
            iconoOjo.className = visible ? 'bi bi-eye-slash toggle-password' : 'bi bi-eye toggle-password text-info';
        });

        function resetFormState() {
            textoBtn.textContent = 'Entrar al sistema';
            spinnerBtn.classList.add('d-none');
            btnSubmit.disabled = false;
        }

        window.addEventListener('pageshow', event => {
            if (event.persisted || (performance && performance.getEntriesByType && performance.getEntriesByType('navigation')[0]?.type === 'back_forward')) {
                window.location.reload();
            }
        });

        document.getElementById('formLogin').addEventListener('submit', async event => {
            event.preventDefault();
            mensajeError.innerHTML = '';
            btnSubmit.disabled = true;
            textoBtn.textContent = 'Validando...';
            spinnerBtn.classList.remove('d-none');

            const formData = new FormData(event.target);
            const response = await fetch(event.target.action, {
                method: 'POST',
                body: formData,
                headers: { 'X-Requested-With': 'XMLHttpRequest' }
            });

            if (!response.ok) {
                mensajeError.innerHTML = `<div class="alert alert-danger rounded-4 py-3">Error del servidor. Intenta nuevamente.</div>`;
                resetFormState();
                return;
            }

            const data = await response.json();
            if (data.success) {
                window.location.href = data.redirect_url;
            } else {
                mensajeError.innerHTML = `<div class="alert alert-danger rounded-4 py-3">${data.mensaje}</div>`;
                resetFormState();
            }
        });
    </script>
</body>
</html>
'''

pages = [
    {
        'filename': 'dashboard.html',
        'title': 'Dashboard',
        'icon': 'bi-speedometer2',
        'subtitle': 'Resumen de la operación, accesos rápidos y métricas clave para tu gestión.',
        'hero': 'Supervisa tu negocio con un panel inteligente.',
        'cards': [
            {'label': 'Usuarios activos', 'count': '128', 'icon': 'bi-people-fill', 'variant': 'bg-info'},
            {'label': 'Productos registrados', 'count': '1,432', 'icon': 'bi-box-seam', 'variant': 'bg-success'},
            {'label': 'Pedidos en proceso', 'count': '16', 'icon': 'bi-cart-check', 'variant': 'bg-warning'},
        ],
        'content': '''
        <div class="row g-4">
            <div class="col-12 col-xl-8">
                <div class="card-surface">
                    <div class="card-body">
                        <div class="d-flex align-items-center justify-content-between mb-4 gap-3">
                            <div>
                                <div class="page-badge">Panel principal</div>
                                <h1 class="page-title mt-3">Bienvenido al dashboard</h1>
                                <p class="text-muted mb-0">Accede rápidamente a tablas, indicadores y acciones del sistema.</p>
                            </div>
                            <a href="{% url 'logout' %}" class="btn btn-outline-light action-button"><i class="bi bi-box-arrow-right me-2"></i>Salir</a>
                        </div>
                        <div class="row row-cols-1 row-cols-md-3 g-3">
                            {% for card in cards %}
                            <div class="col">
                                <div class="p-3 rounded-4 border border-white border-opacity-10 h-100" style="background: rgba(255,255,255,0.03);">
                                    <div class="d-flex align-items-center justify-content-between mb-3">
                                        <span class="badge bg-white bg-opacity-10 text-white"><i class="{{ card.icon }}"></i></span>
                                        <span class="text-muted small">{{ card.label }}</span>
                                    </div>
                                    <div class="d-flex align-items-end justify-content-between">
                                        <div>
                                            <h2 class="mb-1" data-count="{{ card.count }}">{{ card.count }}</h2>
                                            <p class="mb-0 text-muted">Últimas 24 horas</p>
                                        </div>
                                        <div class="rounded-4 p-2 {{ card.variant }} text-white">
                                            <i class="{{ card.icon }} fs-4"></i>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            {% endfor %}
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 col-xl-4">
                <div class="card-surface h-100">
                    <div class="card-body">
                        <div class="d-flex align-items-center justify-content-between mb-4">
                            <div>
                                <span class="page-badge">Accesos rápidos</span>
                                <h2 class="h5 text-white mt-3 mb-2">Navega por las tablas</h2>
                            </div>
                        </div>
                        <div class="d-grid gap-3">
                            <a href="{% url 'personas' %}" class="btn btn-outline-light">Personas</a>
                            <a href="{% url 'productos' %}" class="btn btn-outline-light">Productos</a>
                            <a href="{% url 'pedidos' %}" class="btn btn-outline-light">Pedidos</a>
                            <a href="{% url 'roles' %}" class="btn btn-outline-light">Roles</a>
                        </div>
                    </div>
                </div>
                <div class="card-surface mt-4">
                    <div class="card-body">
                        <h3 class="h6 text-white mb-3">Consejo rápido</h3>
                        <p class="text-muted mb-0">Utiliza el buscador en cada tabla para encontrar registros al instante y evita recargar la página.</p>
                    </div>
                </div>
            </div>
        </div>
    '''
    },
]

records = {
    'usuario.html': {
        'title': 'Usuario',
        'icon': 'bi-person-badge-fill',
        'subtitle': 'Detalle y configuración de los usuarios del sistema.',
        'headers': ['Nombre', 'Correo', 'Rol', 'Estado'],
        'rows': [
            ['Lucas Mendoza', 'lucas@multiblas.com', 'Administrador', '<span class="status-chip status-active">Activo</span>'],
            ['María Torres', 'maria@multiblas.com', 'Vendedor', '<span class="status-chip status-active">Activo</span>'],
            ['Carlos R.', 'carlos@multiblas.com', 'Soporte', '<span class="status-chip status-pending">Pendiente</span>'],
        ]
    },
    'personas.html': {
        'title': 'Personas',
        'icon': 'bi-people-fill',
        'subtitle': 'Registros de clientes, colaboradores y contactos importantes.',
        'headers': ['Nombre', 'Documento', 'Email', 'Teléfono'],
        'rows': [
            ['Ana Pérez', 'DNI 45678912', 'ana.perez@mail.com', '+51 987 654 321'],
            ['Jorge Vega', 'DNI 30214598', 'jorge.vega@mail.com', '+51 946 552 110'],
            ['Elena Ruiz', 'DNI 22113456', 'elena.ruiz@mail.com', '+51 943 214 567'],
        ]
    },
    'metodos_pago.html': {
        'title': 'Métodos de Pago',
        'icon': 'bi-credit-card-2-front-fill',
        'subtitle': 'Administración de formas de pago y estados de cobro.',
        'headers': ['Método', 'Proveedor', 'Moneda', 'Estado'],
        'rows': [
            ['Tarjeta de crédito', 'Visa', 'PEN', '<span class="status-chip status-active">Activo</span>'],
            ['Transferencia', 'BBVA', 'PEN', '<span class="status-chip status-active">Activo</span>'],
            ['Pago móvil', 'Yape', 'PEN', '<span class="status-chip status-pending">Pendiente</span>'],
        ]
    },
    'categorias.html': {
        'title': 'Categorías',
        'icon': 'bi-tags-fill',
        'subtitle': 'Clasificación de productos para facilitar búsquedas y gestión.',
        'headers': ['Categoría', 'Descripción', 'Subcategorías', 'Estado'],
        'rows': [
            ['Hardware', 'Componentes y accesorios', '12', '<span class="status-chip status-active">Activa</span>'],
            ['Software', 'Licencias y servicios', '8', '<span class="status-chip status-active">Activa</span>'],
            ['Servicios', 'Instalación y soporte', '5', '<span class="status-chip status-pending">Pendiente</span>'],
        ]
    },
    'marcas.html': {
        'title': 'Marcas',
        'icon': 'bi-award-fill',
        'subtitle': 'Listado de marcas disponibles en el catálogo.',
        'headers': ['Marca', 'País', 'Productos', 'Estado'],
        'rows': [
            ['Corsair', 'EE.UU.', '34', '<span class="status-chip status-active">Activa</span>'],
            ['ASUS', 'Taiwán', '21', '<span class="status-chip status-active">Activa</span>'],
            ['Microsoft', 'EE.UU.', '14', '<span class="status-chip status-blocked">Bloqueada</span>'],
        ]
    },
    'proveedores.html': {
        'title': 'Proveedores',
        'icon': 'bi-truck-flatbed',
        'subtitle': 'Clientes y proveedores autorizados para compras e inventario.',
        'headers': ['Proveedor', 'Contacto', 'Teléfono', 'País'],
        'rows': [
            ['Global Tech', 'Sofía Díaz', '+51 987 111 222', 'Perú'],
            ['TecnoSupply', 'Mario López', '+51 943 333 444', 'Perú'],
            ['LogiParts', 'Fernando Ruiz', '+1 345 678 901', 'EE.UU.'],
        ]
    },
    'productos.html': {
        'title': 'Productos',
        'icon': 'bi-box-seam',
        'subtitle': 'Inventario completo con estado de stock y precios actualizados.',
        'headers': ['Producto', 'Marca', 'Stock', 'Precio'],
        'rows': [
            ['Memoria RAM 16GB', 'Corsair', '46', 'S/ 289.00'],
            ['Monitor 27" 144Hz', 'ASUS', '17', 'S/ 1,499.00'],
            ['Teclado mecánico', 'LogiTech', '28', 'S/ 249.00'],
        ]
    },
    'pedidos.html': {
        'title': 'Pedidos',
        'icon': 'bi-receipt-cutoff',
        'subtitle': 'Seguimiento rápido del estado de cada pedido en el sistema.',
        'headers': ['Pedido', 'Cliente', 'Total', 'Estado'],
        'rows': [
            ['#1254', 'Luis García', 'S/ 2,450', '<span class="status-chip status-active">Enviado</span>'],
            ['#1255', 'Natalia P.', 'S/ 799', '<span class="status-chip status-pending">Pendiente</span>'],
            ['#1256', 'Raúl F.', 'S/ 1,250', '<span class="status-chip status-active">Completado</span>'],
        ]
    },
    'pagos.html': {
        'title': 'Pagos',
        'icon': 'bi-wallet2',
        'subtitle': 'Historial de pagos y control de cobros realizados.',
        'headers': ['Pago', 'Fecha', 'Monto', 'Método'],
        'rows': [
            ['#P201', '2026-05-15', 'S/ 1,250', 'Yape'],
            ['#P202', '2026-05-14', 'S/ 2,450', 'Transferencia'],
            ['#P203', '2026-05-13', 'S/ 340', 'Tarjeta'],
        ]
    },
    'permisos.html': {
        'title': 'Permisos',
        'icon': 'bi-shield-lock-fill',
        'subtitle': 'Roles y permisos que controlan el acceso al sistema.',
        'headers': ['Permiso', 'Descripción', 'Módulo', 'Nivel'],
        'rows': [
            ['Editar usuarios', 'Modificar datos de usuario', 'Usuarios', 'Alto'],
            ['Ver ventas', 'Acceso a reportes de ventas', 'Ventas', 'Medio'],
            ['Gestionar permisos', 'Asignar roles y accesos', 'Administración', 'Alto'],
        ]
    },
    'detalle_permisos.html': {
        'title': 'Detalle Permisos',
        'icon': 'bi-card-list',
        'subtitle': 'Información detallada de cada permiso y su relación con roles.',
        'headers': ['Permiso', 'Rol', 'Módulo', 'Activo'],
        'rows': [
            ['Editar usuarios', 'Administrador', 'Usuarios', '<span class="status-chip status-active">Sí</span>'],
            ['Ver ventas', 'Vendedor', 'Ventas', '<span class="status-chip status-active">Sí</span>'],
            ['Gestionar permisos', 'Superadmin', 'Administración', '<span class="status-chip status-pending">No</span>'],
        ]
    },
    'roles.html': {
        'title': 'Roles',
        'icon': 'bi-people',
        'subtitle': 'Definición de los roles que usan tus equipos y colaboradores.',
        'headers': ['Rol', 'Descripción', 'Usuarios', 'Estado'],
        'rows': [
            ['Administrador', 'Control total del sistema', '3', '<span class="status-chip status-active">Activo</span>'],
            ['Vendedor', 'Gestiona ventas y clientes', '7', '<span class="status-chip status-active">Activo</span>'],
            ['Soporte', 'Atiende incidencias técnicas', '2', '<span class="status-chip status-pending">Pendiente</span>'],
        ]
    },
    'detalle_roles.html': {
        'title': 'Detalle Roles',
        'icon': 'bi-person-badge',
        'subtitle': 'Relación de cada rol con sus permisos y funciones asignadas.',
        'headers': ['Rol', 'Permiso', 'Tipo', 'Área'],
        'rows': [
            ['Administrador', 'Gestionar permisos', 'Completo', 'Administración'],
            ['Vendedor', 'Ver ventas', 'Lectura', 'Ventas'],
            ['Soporte', 'Atender tickets', 'Ejecutar', 'Soporte'],
        ]
    }
}

def generate_page(file_name, page):
    if file_name == 'dashboard.html':
        cards_markup = '\n'.join([
            f'<div class="col"><div class="p-3 rounded-4 border border-white border-opacity-10 h-100" style="background: rgba(255,255,255,0.03);">'
            f'<div class="d-flex align-items-center justify-content-between mb-3"><span class="badge bg-white bg-opacity-10 text-white"><i class="{card["icon"]}"></i></span><span class="text-muted small">{card["label"]}</span></div>'
            f'<div class="d-flex align-items-end justify-content-between"><div><h2 class="mb-1" data-count="{card["count"]}">{card["count"]}</h2><p class="mb-0 text-muted">Últimas 24 horas</p></div><div class="rounded-4 p-2 {card["variant"]} text-white"><i class="{card["icon"]} fs-4"></i></div></div></div></div>'
            for card in page['cards']])
        content = f"""
        <div class="row g-4">
            <div class="col-12 col-xl-8">
                <div class="card-surface">
                    <div class="card-body">
                        <div class="d-flex align-items-center justify-content-between mb-4 gap-3">
                            <div>
                                <span class="page-badge">Panel principal</span>
                                <h1 class="page-title mt-3">Bienvenido al dashboard</h1>
                                <p class="text-muted mb-0">Accede rápidamente a tablas, indicadores y acciones del sistema.</p>
                            </div>
                            <a href="{% url 'logout' %}" class="btn btn-outline-light action-button"><i class="bi bi-box-arrow-right me-2"></i>Salir</a>
                        </div>
                        <div class="row row-cols-1 row-cols-md-3 g-3">
                            {cards_markup}
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-12 col-xl-4">
                <div class="card-surface h-100">
                    <div class="card-body">
                        <div class="d-flex align-items-center justify-content-between mb-4">
                            <div>
                                <span class="page-badge">Accesos rápidos</span>
                                <h2 class="h5 text-white mt-3 mb-2">Navega por las tablas</h2>
                            </div>
                        </div>
                        <div class="d-grid gap-3">
                            <a href="{% url 'personas' %}" class="btn btn-outline-light">Personas</a>
                            <a href="{% url 'productos' %}" class="btn btn-outline-light">Productos</a>
                            <a href="{% url 'pedidos' %}" class="btn btn-outline-light">Pedidos</a>
                            <a href="{% url 'roles' %}" class="btn btn-outline-light">Roles</a>
                        </div>
                    </div>
                </div>
                <div class="card-surface mt-4">
                    <div class="card-body">
                        <h3 class="h6 text-white mb-3">Consejo rápido</h3>
                        <p class="text-muted mb-0">Usa el buscador de cada tabla para filtrar registros al instante sin recargar.</p>
                    </div>
                </div>
            </div>
        </div>
        """
        page_content = f'''{{% extends 