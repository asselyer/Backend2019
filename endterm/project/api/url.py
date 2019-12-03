from django.urls import path
from api.views import ArticleViewSet
from rest_framework import routers
# from core.views import ProjectListAPIView


# urlpatterns = [
#     path('projects/', ProjectListAPIView.as_view())
# ]

router = routers.DefaultRouter()
router.register('articles', ArticleViewSet, base_name='api')
# router.register('favs', FavoriteViewSet, base_name='api')


urlpatterns = router.urls