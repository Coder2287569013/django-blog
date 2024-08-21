from django.urls import path
from blog import views

urlpatterns = [
    path("", views.post_list, name="post-list"),
    path("post-overview/<int:pk>", views.post_overview, name="post-overview")
]
