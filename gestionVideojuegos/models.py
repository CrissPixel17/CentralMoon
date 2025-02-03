from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="NOMBRE")
    direccion = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

class Videojuegos(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(default="Sin descripción")  # Agregar un valor por defecto
    fecha_lanzamiento = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='videojuegos/', null=True, blank=True)
    precio = models.IntegerField()

    def __str__(self):
        return self.titulo


class Consola(models.Model):
    nombre = models.CharField(max_length=50)
    periodo_duracion = models.CharField(max_length=20)
    descripcion = models.TextField()
    compania = models.CharField(max_length=255)
    imagen = models.ImageField(upload_to="videojuegos/", blank=True, null=True)
    def __str__(self):
        return self.nombre

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()