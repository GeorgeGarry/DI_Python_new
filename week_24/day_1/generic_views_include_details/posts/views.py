from django.shortcuts import get_object_or_404
from django.views import generic

from posts.models import Post


# Create your views here.
class AllPostsPage(generic.ListView):
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    model = Post
    queryset = Post.objects.filter(title='post1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["my_var"] = "this var is custom one"
        return context


class PostPage(generic.DetailView):
    template_name = 'posts/post_details.html'
    model = Post
    context_object_name = 'post'

    def get_object(self, queryset=None):
        id = self.kwargs["id"]
        return get_object_or_404(Post, id=id)
