


from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   	path('', views.index, name='index'),
   	path('newpost/', views.NewPost, name='newpost'),
    path('search_users/', views.Search_users, name='search_users'),
   	
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)