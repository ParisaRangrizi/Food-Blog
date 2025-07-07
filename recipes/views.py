# recipes/views.py
'''this file contains the views for the recipes app'''
from rest_framework import viewsets
from .models import Recipe, RecipeCategory
from .serializers import RecipeSerializer, RecipeCategorySerializer


class RecipeViewSet(viewsets.ModelViewSet):
    '''this class defines the view for listing and creating recipes'''
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeCategoryViewset(viewsets.ModelViewSet):
    queryset = RecipeCategory.objects.all()
    serializer_class = RecipeCategorySerializer
