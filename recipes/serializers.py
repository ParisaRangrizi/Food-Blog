# recipe/serializer.py
'''this module is a serializer for recipe's model'''
from rest_framework import serializers
from . import models


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Recipe
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


class RecipeCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RecipeCategory
        fields = '__all__'
        read_only_fields = ('id', 'slug')