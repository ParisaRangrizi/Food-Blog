# posts/models.py
'''This file defines the models for the posts app.'''
from django.db import models
from users.models import UserProfile


class SocialPost(models.Model):
    '''this class is for the post of the blog'''
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='social_posts')
    image = models.ImageField(upload_to='social_posts/images/')
    caption = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author.user.username}'s Post"

    def __repr__(self):
        return f"Post ('{self.author.user.username}', '{self.caption}', '{self.created_at}')"


class SocialPostLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="post_likes")
    post = models.ForeignKey(SocialPost, on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return f"{self.user.user.username} liked post {self.post.id}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_post_like')
        ]


class SocialPostComment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_post_comments')
    post = models.ForeignKey(SocialPost, on_delete=models.CASCADE, related_name='post_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.user.username} commented on post {self.post.id}"


class PostSave(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_save_posts')
    post = models.ForeignKey(SocialPost, on_delete=models.CASCADE, related_name='saved_posts_users')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_post_save')
        ]

    def __str__(self):
        return f"{self.user.user.username} saved {self.post.author}'s post."
