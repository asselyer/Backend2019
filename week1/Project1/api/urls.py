from django.urls import path, include
from api import views


urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project_detail'),
    path('tasks/', views.TaskList.as_view(), name='task_list'),
    path('tasks/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
    path('block/', views.BlockList.as_view())
]