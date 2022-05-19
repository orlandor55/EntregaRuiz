from django.urls import path
from . import views

app_name = "pages_app"

urlpatterns = [
    path(
        'page-list/', 
        views.PageListView.as_view(),
        name='page-list',
    ),
    path(
        'pages/<slug>/', 
        views.PageDetailView.as_view(),
        name='page-detail',
    ),
    path(
        'create/', 
        views.PageCreateView.as_view(),
        name='page-create',
    ),
]