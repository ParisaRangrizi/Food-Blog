# users/models.py
'''this module is for user models'''
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    '''this class extends the User model to include additional fields'''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='users/profile_pics/', blank=True, null=True)

    class Meta:
        '''this class defines the meta options for the UserProfile model'''
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        db_table = 'user_profile'

    def __str__(self):
        return f"username: {self.user.username}"
