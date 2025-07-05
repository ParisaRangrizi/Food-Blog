'''this module is for user models'''
from django.contrib.auth.models import User


class UserProfile(User):
    '''this class extends the User model to include additional fields'''
    class Meta:
        '''this class defines the meta options for the UserProfile model'''
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
        db_table = 'user_profile'
