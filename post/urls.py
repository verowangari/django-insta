from post.views import  NewPost,PostDetails,tags
from django.urls import path

urlpatterns=[
    # path('',home,name='home'),
    # path('',home, name='home'),
    path('newpost/',NewPost, name='newpost'),
    path('<uuid>:post_id',PostDetails, name='postdetails'),
    path('tag/<slug:tag_slug>',tags, name='tags'),
             
             
             ]