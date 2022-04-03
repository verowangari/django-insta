from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from post.models import Post,Stream

@login_required
def home(request):
    user=request.user
    posts=Stream.objects.filter(user=user)
    
    group_ids=[]
    
    for post in posts:
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')
    
    template=loader.get_template('home.html')
    
    context={
        'post_items':post_items,
    }
    return HttpResponse(template.render(context,request))

# def home(request):
#   template = loader.get_template('home.html')
#   return HttpResponse(template.render())