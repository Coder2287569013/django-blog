from django.db import models
from datetime import timedelta
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, related_name="posts")

    def published_recently(self):
        return timezone.now() - timedelta(days=7) < self.published_date

    def __str__(self):
        return f"{self.title}, {self.published_date}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author_name}, {self.created_at}"