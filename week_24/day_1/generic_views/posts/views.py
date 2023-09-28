from django.views import generic

from posts.models import Post


# Create your views here.
class AllPostsPage(generic.ListView):
    template_name = 'posts/posts.html'
    context_object_name = 'posts'
    model = Post
    # queryset = Post.objects.filter(title='post1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["my_var"] = "this var is custom one"
        return context
