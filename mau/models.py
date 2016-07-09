from django.db import models
from django.utils import timezone


#class# es una palabra clave que indica que estamos definiendo un objeto.
#Post# es el nombre de nuestro modelo. Podemos darle un nombre 
#diferente (pero debemos evitar espacios en blanco y caracteres especiales). 
#Empieza siempre el nombre de una clase con una letra mayúscula.
#models.Model# significa que Post es un modelo de Django, 
#así Django sabe que debe guardarlo en la base de datos.

class Post(models.Model):
    autor = models.ForeignKey('auth.User') #models.ForeignKey es el tipo de dato!
    titulo = models.CharField(max_length=200) #models.CharField es el tipo de dato!
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo