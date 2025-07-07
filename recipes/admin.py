'''this module registers the models with the Django admin site.'''
from django.contrib import admin
from .models import Recipe, RecipeCategory, RecipeComment, RecipeLike, RecipeSave


admin.site.register(Recipe)
admin.site.register(RecipeCategory)
admin.site.register(RecipeComment)
admin.site.register(RecipeLike)
admin.site.register(RecipeSave)
