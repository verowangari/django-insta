# from post.views import index,  NewPost,PostDetails,like
# from django.urls import path

# urlpatterns=[
#     # path('',home,name='home'),
#     # path('',home, name='home'),
#     # path('',index,name='index'),
#     path('newpost/',NewPost, name='newpost'),
#     path('<uuid>:post_id',PostDetails, name='postdetails'),
#     path('tag/<slug:tag_slug>',tags, name='tags'),
#     path('<uuid>:post_id/like',like,name='postlike')
             
             
#              ]



from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   	path('', views.index, name='index'),
   	path('newpost/', views.NewPost, name='newpost'),
   	# path('<uuid:post_id>', PostDetails, name='postdetails'),
   	# path('<uuid:post_id>/like', like, name='postlike'),
   	# path('<uuid:post_id>/favorite', favorite, name='postfavorite'),
   	# path('tag/<slug:tag_slug>', tags, name='tags'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)