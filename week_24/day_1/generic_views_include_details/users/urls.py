from django.urls import path
from users.views import AllUsersPage, UserPage

urlpatterns = [
    # path('allusers/', AllUsersPage.as_view(), name='users'),
    path('/<int:id>/', UserPage.as_view(), name='users')
]
