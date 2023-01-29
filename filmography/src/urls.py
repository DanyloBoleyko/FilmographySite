from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views.index import index
from .views.film_details import film_details
from .views.person_details import person_details

urlpatterns = [
    path('', index, name='home'),
    path('film/<int:key>', film_details, name='film_details'),
    path('person/<int:key>', person_details, name='person_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
