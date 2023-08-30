

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('person/', views.display_person),
    path('people/', views.display_people),
    path('all_people/', views.display_all_people)


]
