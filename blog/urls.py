from django.urls import path
from blog.views import IndexView, PostDetailView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="post-detail")
]

app_name = "blog"
