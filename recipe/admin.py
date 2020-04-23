from django.contrib import admin

# Register your models here.

# Register your models here.
from recipe.models import Ingredient, Recipe


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = ['title', 'uuid']
    readonly_fields = ['uuid']
    search_fields = ['title']


# admin.site.register(Ingredient)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['title', 'uuid', 'owner', 'ingredients']
    # filter_horizontal = ('ingredients',)
    readonly_fields = ['uuid']

    autocomplete_fields = ['owner','ingredients']