from django.shortcuts import render
from django.http import HttpResponse, Http404

from recipe.models import Recipe


def index(request):
    return HttpResponse("Recipe")


def detail(request, recipe_id):
    try:
        # s = Recipe.objects.filter(id=recipe_id)
        # o = s.get()
        o = Recipe.objects.get(id=recipe_id)

    except Recipe.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    return render(request, 'recipe/detail.html', {
        'title': o.title,
    })


    # try:
    #     # s = Recipe.objects.filter(id=recipe_id)
    #     # o = s.get()
    #     o = Recipe.objects.get(id=recipe_id)
    #
    # except Recipe.DoesNotExist:
    #     raise Http404("No MyModel matches the given query.")
    #
    # return HttpResponse("Recipe %s" % o.title)