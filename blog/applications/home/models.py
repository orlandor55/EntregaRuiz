from django.db import models
from model_utils.models import TimeStampedModel


class Home(TimeStampedModel):
    """Modelo para la pantalla de home"""

    title = models.CharField(
        'Nombre',
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Título Nosotros',
        max_length=50
    )
    about_tex = models.TextField()
    contact_email = models.EmailField(
        'email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Teléfono de contacto',
        max_length=20
    )

    class Meta:
        verbose_name = 'Página Principal'
        verbose_name_plural = 'Página Principal'

    def __str__(self):
        return self.title


class Suscribers(TimeStampedModel):
    """Modelo para suscriptores"""

    email = models.EmailField()

    class Meta:
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'

    def __str__(self):
        return self.email


class Contact(TimeStampedModel):
    """Modelo para formulario de contacto"""
    
    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.full_name
