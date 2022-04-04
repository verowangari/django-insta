from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.template import loader

# Create your views here.
from post.models import Post,Stream,Tag
from post.forms import NewPostForm
from django.http import HttpResponseRedirect,HttpResponse



# @login_required
# def index(request):
#     post_items = Post.objects.all()
#     return render(request, 'home.html',{'post_items':post_items[::-1],})
# def home(request):
#   template = loader.get_template('home.html')
#   return HttpResponse(template.render())

@login_required
def index(request):
    user=request.user
    posts=Stream.objects.filter(user=user)
    
    group_ids=[]
    
    for post in posts:
        group_ids.append(post.post_id)

    post_items = Post.objects.all()
    template=loader.get_template('home.html')

    context={
    'post_items':post_items,
}

    return HttpResponse(template.render(context,request))

# @login_required
# def NewPost(request):
#     if request.method == 'POST':
#         data=request.POST
#         images=request.FILES.getlist('pictures')
#         form = NewPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = Post(file_field=request.FILES['file'])
#             instance.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = NewPostForm()
#     return render(request, 'newpost.html', {'form': form})

def NewPost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NewPostForm()
    return render(request, 'newpost.html', {
        'form': form
    })