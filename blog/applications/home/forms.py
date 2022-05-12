from django import forms

#models
from .models import Suscribers, Contact

class SuscribersForm(forms.ModelForm):
    """Definición de formulario para Suscribers"""

    class Meta:
        """Definición de los Meta para el Suscribersform."""

        model = Suscribers
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electrónico...',
                }
            )
        }


class ContactForm(forms.ModelForm):
    """Definiciones del formulario de contacto."""

    class Meta:
        """Definición de los Meta del Contactform."""

        model = Contact
        fields = ('__all__')
