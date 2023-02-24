from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .views.franchise_details import franchise_details
from .views.index import index
from .views.film_details import film_details
from .views.person_details import person_details
from .views.profile import profile
from .views.search import search

urlpatterns = [
    path('', index, name='home'),
    path('film/<int:key>', film_details, name='film_details'),
    path('person/<int:key>', person_details, name='person_details'),
    path('franchise/<int:key>', franchise_details, name='franchise_details'),
    path('search/<str:text>', search, name='search'),
    path('user/', include('django.contrib.auth.urls')),
    path('user/profile/', profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
