from django.shortcuts import render
from blog import models
# Create your views here.

def posts_list(request):
    posts = models.Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, "blog/posts-list.html", context)