from django.urls import path
from posts.views import AllPostsPage, PostPage

urlpatterns = [
    path('all/', AllPostsPage.as_view(), name='posts'),
    path('<int:id>/', PostPage.as_view(), name='posts')
]
