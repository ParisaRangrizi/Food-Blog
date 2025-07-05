'''This file defines the models for the posts app.'''
from django.db import models
from users.models import UserProfile


class PostCategory(models.Model):
    '''this class is for category of the food'''
    name = models.CharField(max_length=100)
    description = models.CharField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        '''this is method for show the info of the class'''
        return f'category:{self.name}'


class Post(models.Model):
    '''this class is for the post of the blog'''
    category = models.ManyToManyField(PostCategory)
    title = models.CharField(max_length=20, blank=True, null=True)
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/images/', blank=True)
    created_at = models.DateField(auto_now_add=True)
    edited_at = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts_author')

    def __str__(self):
        return f'post:{self.title}'


class PostComment(models.Model):
    '''this class is for the comments on the blog's posts'''
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_post_comments')

    def __str__(self):
        return f'Comment by {self.user} on {self.post}'


class PostLike(models.Model):
    '''this class is for the likes of the recipes and posts'''
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')