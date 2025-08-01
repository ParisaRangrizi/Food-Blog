'''this module registers the models with the Django admin site.'''
from django.contrib import admin
from .models import SocialPost, SocialPostLike, SocialPostComment, PostSave


admin.site.register(SocialPost)
admin.site.register(SocialPostLike)
admin.site.register(SocialPostComment)
admin.site.register(PostSave)
