from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns_local = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.home.urls')),
    #re_path('', include('applications.entrada.urls')),
    #re_path('', include('applications.favoritos.urls')),

]

urlpatterns_terceros = [
    # urls para ckeditor
    re_path(r'ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns = urlpatterns_local + urlpatterns_terceros