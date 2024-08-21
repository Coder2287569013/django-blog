from django.shortcuts import render
from blog import models
from django.http import HttpResponse
# Create your views here.

def post_list(request):
    posts = models.Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, "blog/post_list.html", context)

def post_overview(request, pk):
    try:
        post = models.Post.objects.get(id=pk)
    except models.Post.DoesNotExist:
        HttpResponse("Post doesn't exist", 404)
    
    context = {
        "post_info": post
    }

    return render(request, "blog/post_overview.html", context)
