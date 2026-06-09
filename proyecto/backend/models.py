import uuid
from django.db import models
from django.contrib.auth.models import User # Si no usas User abajo, puedes borrar esta línea
from p.models import Personas

# --- 1. MODELOS DE SOPORTE ---

class MetodoPago(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=50, unique=True)
    instrucciones = models.TextField(blank=True, null=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='categorias/', blank=True, null=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, unique=True)
    pais_origen = models.CharField(max_length=100, blank=True, null=True)
    sitio_web = models.URLField(max_length=255, blank=True, null=True)
    estado = models.BooleanField(default=True)
    destacado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Sin cascada: PROTECT
    persona = models.ForeignKey(Personas, on_delete=models.PROTECT, related_name='proveedores')
    nombre_empresa = models.CharField(max_length=150)
    ruc = models.CharField(max_length=11, unique=True)
    direccion_empresa = models.CharField(max_length=255)
    telefono_contacto = models.CharField(max_length=15)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_empresa

# --- 2. INVENTARIO Y VENTAS ---

class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    persona = models.ForeignKey(Personas, on_delete=models.PROTECT)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, default='pendiente')
    nro_pedido = models.PositiveIntegerField(unique=True, null=True)

    def __str__(self):
        return f"Pedido {self.nro_pedido}"

class Pago(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.PROTECT)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    nro_operacion = models.CharField(max_length=100, blank=True, null=True)
    comprobante_pago = models.ImageField(upload_to='pagos/vouchers/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    confirmado = models.BooleanField(default=False)