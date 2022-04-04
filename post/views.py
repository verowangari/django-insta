from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from post.models import Post,Stream,Tag
from post.forms import NewPostForm

@login_required
def index(request):
    post_items = Post.objects.all()
    return render(request, 'home.html',{'post_items':post_items[::-1],})
# def home(request):
#   template = loader.get_template('home.html')
#   return HttpResponse(template.render())


@login_required
def NewPost(request):
    user=request.user.id
    tags_objs=[]