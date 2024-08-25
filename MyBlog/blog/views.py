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
        "post_info": post,
        "published_recently": post.published_recently(),
        "comments": post.comments.all()
    }

    return render(request, "blog/post_overview.html", context)

def authors_posts(request, pk):
    try:
        author = models.Author.objects.get(id=pk)
    except models.Author.DoesNotExist:
        HttpResponse("Author doesn't exist", 404)
    
    context = {
        "author_posts": author.posts.all()   
    }

    return render(request, "blog/authors_posts.html", context)