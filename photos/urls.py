from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^nairobi/', views.nairobi, name='nairobi'),
    url(r'^rio/', views.rio, name='rio'),
    url(r'^tokyo/', views.tokyo, name='tokyo'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)