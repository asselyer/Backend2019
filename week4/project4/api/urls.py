from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from api import views


urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.RegisterUser.as_view()),
    path('profile/<str:user__username>', views.ProfileView.as_view()),
    # path('profile/<int:id>', views.ProfileEdit.as_view(), name='profile_edit'),

    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project_detail'),
    path('tasks/', views.TaskList.as_view(), name='task_list'),
    path('projects/<int:pk>/tasks/', views.ProjectTasksList.as_view(), name='project_task_list'),
    path('tasks/<int:pk>', views.TaskDetail.as_view(), name='task_detail'),
    path('block/', views.BlockList.as_view())
]


router = DefaultRouter()
router.register('users', views.UserViewSet, base_name='users'),


urlpatterns += router.urls

Java:
int a = 1

Python:
a = 1