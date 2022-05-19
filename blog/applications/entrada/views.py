from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)

#models
from .models import Category, Entry
#forms
from .forms import EntryForm

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from applications.page.views import StaffRequiredMixin
from django.urls import reverse_lazy

class EntryListView(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    pagintated_by = 7

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        return context
    

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria", '')
        queryset = Entry.objects.buscar_entrada(kword, categoria)

        return queryset



class EntryDetailView(DetailView):
    model = Entry
    template_name = "entrada/detail.html"


@method_decorator(staff_member_required, name='dispatch')
class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = "entrada/entry_create.html"
    success_url = reverse_lazy('entrada_app:entry-list')

