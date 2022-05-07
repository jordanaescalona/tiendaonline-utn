from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=150,unique=True)
    activo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nombre
    
class Subcategoria(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria,related_name='SubCategoria_Categoria',on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return '{}:{}'.format(self.categoria.nombre,self.nombre)
    
    class Meta:
        unique_together = ('categoria','nombre')

