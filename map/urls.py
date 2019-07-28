from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'map'

urlpatterns = [
    path('', views.main, name='main'),
    path('mapbox/', views.mapbox, name='mapbox'),
    path('local_search/', views.local_search, name='local_search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
