 #
from django.urls import path
from . import views

app_name = "favorites_app" 

urlpatterns = [
    path(
        'profile/', 
        views.UserPageListView.as_view(),
        name='profile',
    ),
    path(
        'add-favorite-entry/<slug>/', 
        views.AddFavoriteView.as_view(),
        name='add-favorites',
    ),
    path(
        'delete-favorite-entry/<pk>/', 
        views.FavoritesDeleteView.as_view(),
        name='delete-favorites',
    ),
]