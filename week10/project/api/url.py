from django.urls import path
from api.views import ProjectListViewSet, ProjectViewSet, TaskViewSet
from rest_framework import routers
# from core.views import ProjectListAPIView


# urlpatterns = [
#     path('projects/', ProjectListAPIView.as_view())
# ]

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, base_name='api')
router.register('tasks', TaskViewSet, base_name='api')


urlpatterns = router.urls