from django.urls import path
from .views import HomePageView, FilmCreateView, DirectorCreateView, ReviewCreateView

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('addDirector/', DirectorCreateView.as_view(), name='adddirector'),
    path('addFilm/', FilmCreateView.as_view(), name='addfilm'),
    path('addReview/', ReviewCreateView.as_view(), name='addreview')
]
