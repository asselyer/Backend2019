from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from api.views import RegisterUser, UserViewSet, ProductViewSet, ServiceViewSet, ProductList, ServiceList

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', RegisterUser.as_view()),

    path('products/', ProductList.as_view()),
    path('services/', ServiceList.as_view())


]


router = DefaultRouter()
router.register('users', UserViewSet, base_name='users'),
router.register('product', ProductViewSet,base_name='api'),
router.register('service', ServiceViewSet,base_name='api')

urlpatterns += router.urls