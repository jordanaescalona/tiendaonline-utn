from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Categoria, Subcategoria
from .forms import CategoriaForm

# Create your views here.
class CategoriaView(LoginRequiredMixin,generic.ListView):
    model = Categoria
    template_name = 'inventario/categoria_list.html'
    context_object_name = "obj"
    login_url = "administracion:login"

class CategoriaNew(LoginRequiredMixin,generic.CreateView):
    model = Categoria
    template_name = 'inventario/categoria.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy('inventario:categorias')
    login_url = "administracion:login"

class CategoriaUpdate(LoginRequiredMixin,generic.UpdateView):
    model = Categoria
    template_name = 'inventario/categoria.html'
    context_object_name = "obj"
    form_class = CategoriaForm
    success_url = reverse_lazy('inventario:categorias')
    login_url = "administracion:login"

class CategoriaDelete(LoginRequiredMixin,generic.DeleteView):
    model = Categoria
    template_name = 'inventario/eliminar.html'
    context_object_name = "obj"
    
    success_url = reverse_lazy('inventario:categorias')
    login_url = "administracion:login"

class SubcategoriaView(LoginRequiredMixin,generic.ListView):
    model = Subcategoria
    template_name = 'inventario/subcategoria_list.html'
    context_object_name = "obj"
    login_url = "administracion:login"

class SubcategoriaNew(LoginRequiredMixin,generic.CreateView):
    model = Subcategoria
    template_name = 'inventario/subcategoria.html'
    


