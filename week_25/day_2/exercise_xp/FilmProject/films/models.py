from django.core.validators import MaxValueValidator,MinValueValidator
from django.db import models
from django.utils import timezone


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Director(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Film(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField(default=timezone.now)
    created_in_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="films_created")
    available_in_countries = models.ManyToManyField(Country, related_name="films_available")
    category = models.ManyToManyField(Category, related_name="films")
    director = models.ManyToManyField(Director, related_name="films")

    def __str__(self):
        return self.title


class Review(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name="film")
    review_text = models.CharField(max_length=255)
    rating = models.IntegerField(default=1 ,validators=[MaxValueValidator(5), MinValueValidator(1)])
    review_date = models.DateField(default=timezone.now)
