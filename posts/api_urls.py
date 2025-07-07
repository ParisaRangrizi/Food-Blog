# # posts/api_urls.py
from rest_framework.routers import DefaultRouter
from . import views


ruoter = DefaultRouter()

ruoter.register(r'socialposts', views.SocialPostViewSet, basename='socialpost')

urlpatterns = ruoter.urls
