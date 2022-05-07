from django import forms
from .models import Categoria


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

        widgets = {
            'nombre':forms.TextInput(attrs={
                'class': 'form-control mr-5'
            }),
            'activo':forms.CheckboxInput(attrs={
                'class':' form-check-input'
            })

        }


 