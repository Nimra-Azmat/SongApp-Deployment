from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('artists/', include('artists.urls'), name='artist'),
    path('albums/', include('albums.urls'), name='album'),
    path('songs/', include('songs.urls'), name='song'),
    path('api/', include('base.api.urls'), name='base'),

]
