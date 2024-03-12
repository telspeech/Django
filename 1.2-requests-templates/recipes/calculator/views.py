from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def index(request, recipe):
    servings = int(request.GET.get('servings', 1))

    if recipe in DATA:
        original_recipe = DATA[recipe]
        adjusted_recipe = {ingredient: amount * servings for ingredient, amount in original_recipe.items()}
        context = {'recipe': adjusted_recipe}
    else:
        context = {'recipe': {}}

    return render(request, 'calculator/index.html', context)
