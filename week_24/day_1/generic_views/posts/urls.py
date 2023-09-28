from django.urls import path
from posts.views import AllPostsPage

urlpatterns = [
    path('all/', AllPostsPage.as_view(), name='posts')
]
