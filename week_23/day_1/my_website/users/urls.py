from django.urls import path
from users import views

urlpatterns = [
    path('profile_user/<name>', views.profile_user, name='profile_user'),
]
