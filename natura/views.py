from django.shortcuts import render
from django.http import HttpResponse
from natura.models import Producto, Profile, Mensaje
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, 'natura/about.html')


def index(request):
    context = {
        "productos": Producto.objects.all()
    }
    return render(request, 'natura/index.html', context)


""" ------------------- CRUD PRODUCT ----------------------- """
class ProductList(ListView):
    model = Producto
    #Producto.objects.all()

class ProductDetail(DetailView):
    model = Producto
    #Producto.objects.get(id=pk)

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Producto
    success_url = reverse_lazy('productos-list')
    fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen']
    
    def form_valid(self, form):
        form.instance.publicado = self.request.user
        return super().form_valid(form)

class ProductUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Producto
    success_url = reverse_lazy('productos-list')
    fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen']
    
    def form_valid(self, form):
        form.instance.publicado = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        user_id = self.request.user.id
        product_id = self.kwargs.get('pk')
        return Producto.objects.filter(publicado=user_id, id=product_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, 'natura/not_found.html')


class ProductDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('productos-list')
    
    def test_func(self):
        user_id = self.request.user.id
        product_id = self.kwargs.get('pk')
        return Producto.objects.filter(publicado=user_id, id=product_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, 'natura/not_found.html')


""" ------------------- SIGN UP ----------------------- """
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')


""" ------------------- LOGIN-LOGOUT----------------------- """
class Login(LoginView):
    next_page = reverse_lazy('index')

class Logout(LogoutView):
    template_name = 'registration/logout.html'


""" ------------------- CRUD PROFILE ----------------------- """
class ProfileList(ListView):
    model = Profile


class ProfileDetail(DetailView):
    model = Profile


class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy('profile-list')
    fields = '__all__'


class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    fields = '__all__'
    
    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, 'natura/not_found.html')


class ProfileDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('productos-list')
    
    def test_func(self):
        user_id = self.request.user.id
        profile_id = self.kwargs.get('pk')
        return Profile.objects.filter(user=user_id, id=profile_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, 'natura/not_found.html')

""" ------------------ MENSAJES ---------------------- """

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy('mensaje-enviado')

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = 'mensaje'
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()

class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-list')
    
    def test_func(self):
        user_id = self.request.user.id
        mensajes_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id).exists()

def mensajeEnviado(request):
    return render(request, 'natura/mensaje_enviado.html')