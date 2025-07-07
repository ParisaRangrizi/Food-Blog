from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register(r'recipes', views.RecipeViewSet, basename='recipe')
router.register(r'categories', views.RecipeCategoryViewset, basename='recipecategory')

urlpatterns = router.urls
