from django.urls import path
from . import views
from django.contrib.auth import views as authViews 
from clone.views import Signup
urlpatterns=[
    # path('', views.index, name='index'),
    
    path('signup/', Signup, name='signup'),
    # path('profile/edit', EditProfile, name='edit-profile'),
    path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
   	
]