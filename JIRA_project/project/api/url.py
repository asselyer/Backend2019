from django.urls import path
from api.views import ProjectListViewSet, ProjectViewSet, TaskViewSet, TaskDocumentAPIView, TaskCommentAPIView, ProjectMemberView, BlockDetailViewSet, BlockListViewSet, TaskCommentCreateView, TaskDocumentCreateView
from rest_framework import routers


urlpatterns = [
    path('blocks/', BlockListViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('blocks/<int:pk>', BlockDetailViewSet.as_view({'put': 'update', 'delete':'destroy'})),
    path('task/comment', TaskCommentCreateView.as_view()),
    path('task/document', TaskDocumentCreateView.as_view()),

]

router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, base_name='api')
router.register('tasks', TaskViewSet, base_name='api')


urlpatterns += router.urls