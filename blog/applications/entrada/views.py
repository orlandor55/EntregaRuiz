from unicodedata import category
from django.shortcuts import render
from django.views.generic import (
    ListView,
)

#models
from .models import Category, Entry



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

