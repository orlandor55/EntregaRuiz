from django import forms

#models
from .models import Suscribers

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
