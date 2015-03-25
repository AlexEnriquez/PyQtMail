from django.db import models

# Create your models here.
"""class Remitente(models.Model):
    nombre=models.TextField(max_length=200)
    correo=models.TextField(max_length=200)

    def __unicode__(self):
        return self.nombre

class Destinatario(models.Model):
    nombre = models.TextField(max_length=200)
    correo= models.TextField(max_length=200)

    def __unicode__(self):
        return self.nombre"""

class Mail(models.Model):
    remitente = models.TextField(max_length=200)
    destinatario = models.TextField(max_length=200)
    asunto = models.TextField(max_length=200)
    mensaje= models.TextField(max_length=1500)
