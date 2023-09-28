from django.shortcuts import render
from django.views import generic

from users.models import Person


# Create your views here.
class AllUsersPage(generic.ListView):
    template_name = 'users.html'
    context_object_name = 'person'
    model = Person
    # queryset = Post.objects.filter(title='post1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["my_var"] = "this var is custom one"
        return context


class UserPage(generic.DetailView):
    template_name = 'users/users_details.html'
    model = Person
    context_object_name = 'post'

    def get_object(self, queryset=None):
        id = self.kwargs["id"]
        return get_object_or_404(Person, id=id)
