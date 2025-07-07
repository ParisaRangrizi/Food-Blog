from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'userprofiles', views.UserProfileViewset, basename='userprofile')
router.register(r'users', views.UserProfileViewset, basename='user')

urlpatterns = router.urls
