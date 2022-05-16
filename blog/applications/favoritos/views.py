from django.forms import SlugField
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    View,
    ListView,
    DeleteView
)

# models
from .models import Favorites
from applications.entrada.models import Entry


class UserPageListView(LoginRequiredMixin, ListView):
    template_name = "favoritos/profile.html"
    context_object_name = 'entradas_user'
    login_url = reverse_lazy('users_app:user-login')

    def get_queryset(self):
        return Favorites.objects.entradas_user(self.request.user)
    

class AddFavoriteView(LoginRequiredMixin, View):

    login_url = reverse_lazy('users_app:user-login')

    def post(self, request, *args, **kwargs):
        
        usuario = self.request.user
        entrada = Entry.objects.get(slug=self.kwargs['slug'])
        try:
            Favorites.objects.create(
            user=usuario,
            entry=entrada,
            )
            return HttpResponseRedirect(
            reverse(
                'favorites_app:profile'
                )
             )
        except:
            return HttpResponseRedirect(
            reverse(
                'favorites_app:profile'
                )
             )


class FavoritesDeleteView(DeleteView):
    model = Favorites
    success_url = reverse_lazy('favorites_app:profile')
