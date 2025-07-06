# recipe/models.py
'''this file contains the models for the recipes app'''
from django.db import models
from users.models import UserProfile


class DifficultyLevel(models.TextChoices):
    EASY = 'easy', 'Easy'
    MEDIUM = 'medium', 'Medium'
    HARD = 'hard', 'Hard'


class Recipe(models.Model):
    '''this class defines the Recipe model'''
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='recipes/images/', blank=True, null=True)
    ingredients = models.TextField()
    born_city = models.CharField(max_length=50)
    steps = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DifficultyLevel.choices, default=DifficultyLevel.MEDIUM)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='recipes')

    class Meta:
        '''this class defines the meta options for the Recipe model'''
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        db_table = 'recipe'
        ordering = ['-created_at']

    def __str__(self):
        '''this method returns the string representation of the Recipe model'''
        return self.title

    def __repr__(self):
        return f"Recipe ('{self.title}', '{self.author.user.username}', '{self.created_at}')"


class RecipeCategory(models.Model):
    '''this class defines the RecipeCategory model'''
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    recipes = models.ManyToManyField(Recipe, related_name='recipe_categories')
    slug = models.SlugField(max_length=100, unique=True, help_text='A short label for URL purposes')
    image = models.ImageField(upload_to='recipe_categories/images/', blank=True, null=True)

    class Meta:
        '''this class defines the meta options for the RecipeCategory model'''
        verbose_name = 'Recipe Category'
        verbose_name_plural = 'Recipe Categories'
        db_table = 'recipe_category'

    def __str__(self):
        '''this method returns the string representation of the RecipeCategory model'''
        return self.name


class RecipeComment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='author_recipe_comments')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_comments')
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.user.user.username} on {self.recipe.title}"


class RecipeLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_recipe_likes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_likes')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'], name='unique_recipe_like')
        ]

    def __str__(self):
        return f"{self.user.user.username} likes {self.recipe.title}"


class RecipeSave(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_save_recipes')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='saved_recipe_users')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'recipe'], name='unique_recipe_save')
        ]

    def __str__(self):
        return f"{self.user.user.username} saved {self.recipe.title}"
