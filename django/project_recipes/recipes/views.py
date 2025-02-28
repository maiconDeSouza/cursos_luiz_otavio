from django.shortcuts import render


def index(request):
    return render(request, 'recipes/pages/index.html')


def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html')
