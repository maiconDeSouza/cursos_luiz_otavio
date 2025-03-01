from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Recipe


def index(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    context = {
        'recipes': recipes,
        'title': 'Recipes'
    }
    return render(request, 'recipes/pages/index.html', context)


def recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, is_published=True)
    context = {
        'recipe': recipe,
        'title': f'Recipe | {recipe.title}'
    }
    return render(request, 'recipes/pages/recipe.html', context)


def category(request, name):
    # category_filter = Recipe.objects.filter(category__name=name)
    # category_filter = get_list_or_404(Recipe, category__name=name)
    category_filter = get_list_or_404(
        Recipe.objects.filter(category__name=name).order_by('-id'))
    context = {
        'recipes': category_filter,
        'title': f'Recipes | {name}'
    }

    return render(request, 'recipes/pages/index.html', context)
