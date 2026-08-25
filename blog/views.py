from django.shortcuts import redirect
from django.views import generic

from blog.models import Post, User, Commentary


class IndexView(generic.ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by("-created_time")


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        content = request.POST.get("comment")
        if content:
            Commentary.objects.create(
                post=post,
                user=request.user,
                content=content
            )

        return redirect(request.path)
