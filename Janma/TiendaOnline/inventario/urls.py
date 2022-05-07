from django.urls import path
from .views import CategoriaView,CategoriaNew,CategoriaUpdate,CategoriaDelete
from .views import SubcategoriaView
app_name = "inventario"

urlpatterns = [
    #CATEGORIAS
    path('categorias/',CategoriaView.as_view(),name="categorias"),
    path('categorias/nueva',CategoriaNew.as_view(),name="categoria_nueva"),
    path('categorias/nueva/<int:pk>',CategoriaUpdate.as_view(),name="categoria_editar"),
    path('categorias/delete/<int:pk>',CategoriaDelete.as_view(),name="categoria_eliminar"),
    #SUBCATEGORÍAS
    path('subcategorias/',SubcategoriaView.as_view(),name="subcategorias"),
]