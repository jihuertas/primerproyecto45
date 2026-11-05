from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor',on_delete=models.CASCADE, related_name='posts')
    cuerpo = models.TextField()
    categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, related_name='posts')
    imagen = models.ImageField()
    def __str__(self) -> str:
        return f"{self.titulo} ({self.autor})"

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.apellidos}, {self.nombre}"
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.nombre}"