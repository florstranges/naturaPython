from django.shortcuts import render
from django.http import HttpResponse
from natura.models import Producto, Consultora, Cliente
from natura.forms import ProductoForm, BuscarProductoForm, ConsultoraForm, BuscarConsultoraForm, ClienteForm, BuscarClienteForm
from django.views.generic import ListView

def index(request):
    return render(request, 'natura/index.html')

def mostrar_mis_productos(request):
    productos = Producto.objects.all()
    
    context ={
        'productos': productos,
        'form': ProductoForm(),
    }
    return render(request, 'natura/productos.html', context)


""" ---------------------------- Cargar Producto -------------------------------------------- """
def cargar_producto(request):
    f = ProductoForm(request.POST)    
    context = {
        'form': f,
    }


    if f.is_valid():
        Producto(nombre = f.data['nombre'], categoria = f.data['categoria']).save()
        context['form'] = ProductoForm()
    
    context['productos'] = Producto.objects.all()
    
    return render(request, 'natura/productos.html', context)

""" ---------------------------- Buscar Producto -------------------------------------------- """
class BuscarProducto(ListView):
    model = Producto
    context_object_name = 'productos'
    
    def get_queryset(self):
        f = BuscarProductoForm(self.request.GET)
        if f.is_valid():
            return Producto.objects.filter(nombre__icontains=f.data['criterio_nombre']).all()
        return Producto.objects.none()



""" ---------------------------- Cargar Consultora -------------------------------------------- """
def cargar_consultora(request):
    f = ConsultoraForm(request.POST)    
    context = {
        'form': f,
    }


    if f.is_valid():
        Consultora(nombre = f.data['nombre'], apellido = f.data['apellido'], codigoCN = f.data['codigoCN'], zona = f.data['zona']).save()
        context['form'] = ConsultoraForm()
    
    context['consultoras'] = Consultora.objects.all()
    
    return render(request, 'natura/consultora.html', context)

""" ---------------------------- Buscar Consultora -------------------------------------------- """
class BuscarConsultora(ListView):
    model = Consultora
    context_object_name = 'consultoras'
    
    def get_queryset(self):
        f = BuscarConsultoraForm(self.request.GET)
        if f.is_valid():
            return Consultora.objects.filter(nombre__icontains=f.data['criterio_nombre']).all()
        return Consultora.objects.none()



""" ---------------------------- Cargar Cliente -------------------------------------------- """
def cargar_cliente(request):
    f = ClienteForm(request.POST)    
    context = {
        'form': f,
    }


    if f.is_valid():
        Cliente(nombre = f.data['nombre'], apellido = f.data['apellido'], telefono = f.data['telefono'], pedido = f.data['pedido'], consultora = f.data['consultora']).save()
        context['form'] = ClienteForm()
    
    context['clientes'] = Cliente.objects.all()
    
    return render(request, 'natura/cliente.html', context)

""" ---------------------------- Buscar Cliente -------------------------------------------- """
class BuscarCliente(ListView):
    model = Cliente
    context_object_name = 'clientes'
    
    def get_queryset(self):
        f = BuscarClienteForm(self.request.GET)
        if f.is_valid():
            return Cliente.objects.filter(nombre__icontains=f.data['criterio_nombre']).all()
        return Cliente.objects.none()