from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Film, Director, Review
from .forms import FilmForm, DirectorForm, ReviewForm


# Create your views here.

class HomePageView(generic.ListView):
    template_name = 'films/homepage.html'
    context_object_name = 'all_films'

    def get_queryset(self):
        films_with_reviews = []
        films = Film.objects.all()

        for film in films:
            reviews = film.film.all()  # Get the related reviews for each film
            films_with_reviews.append((film, reviews))

        return films_with_reviews
    print(get_queryset)

class FilmCreateView(generic.CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'film/addFilm.html'
    success_url = reverse_lazy('homepage')


class DirectorCreateView(generic.CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'director/addDirector.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        director_to_add = form.cleaned_data
        print(director_to_add)
        return super().form_valid(form)


class ReviewCreateView(generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review/addReview.html'
    success_url = reverse_lazy('homepage')
