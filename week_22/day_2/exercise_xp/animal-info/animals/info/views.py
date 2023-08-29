from django.shortcuts import render
from .data import animals, families


# from templates import *
# from django.http import HttpResponse

# Create your views here.

def display_all_animals(request):
    # should show a list of all the animals. Display all the information :
    # name, legs, weight, height and speed
    context = {
        'animals': animals
    }
    return render(request, 'all_animals.html', context)


def display_all_families(request):
    context = {
        'families': families
    }
    return render(request, 'all_families.html', context)


def display_one_animal(request, animal_id):
    filtered_animal = [animal for animal in animals if animal['id'] == animal_id]
    context = {
        'filtered_animal': filtered_animal
    }
    return render(request, 'animal.html', context)

def display_animal_per_family(request, family_id):
    # family_select = [families for families in families if families["id"] == family_id]
    filtered_animal_family = [animal for animal in animals if animal['family'] == family_id]
    context = {
        'filtered_animal_family': filtered_animal_family
    }
    return render(request, 'animals_in_family.html', context)
