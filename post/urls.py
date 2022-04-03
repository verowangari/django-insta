from post.views import home, NewPost
from django.urls import path

urlpatterns=[
    # path('',home,name='home'),
    path('',home, name='home'),
    path('newpost/',NewPost, name='newpost'),
             
             
             ]