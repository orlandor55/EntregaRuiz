from django.views.generic import (
    TemplateView,
    CreateView
)

#apps entrada

from applications.entrada.models import Entry

# models
from .models import Home, Contact
#forms
from .forms import SuscribersForm, ContactForm  

class HomePageView(TemplateView):
    template_name = "home/index.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #carga del home
        context['home'] = Home.objects.latest('created')
        #contexto para la entrada de la portada
        context["portada"] = Entry.objects.entrada_en_portada()
        #contexto para las entradas recientes
        context["entradas_recientes"] = Entry.objects.entradas_recientes()
        #envío de form de suscripción
        context["home_form"] = SuscribersForm

        return context
    


class SuscriberCreateView(CreateView):
    form_class = SuscribersForm
    success_url ='.'



class ContactCreateView(CreateView):
    form_class = ContactForm
    success_url ='.'
