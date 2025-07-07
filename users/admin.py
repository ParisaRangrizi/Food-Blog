'''this module registers the models with the Django admin site.'''
from django.contrib import admin
from .models import UserProfile


admin.site.register(UserProfile)
