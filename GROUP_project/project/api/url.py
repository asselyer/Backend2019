from django.urls import path
from rest_framework import routers
from api.views import PostMediafileCreateView, PostCommentCreateView, BlogCategoryAPIView, BlogCategoryDetailAPIView, FavoritePostsDetailViewSet, FavoritePostsViewSet, BlogViewSet, PostViewSet

urlpatterns = [
    path('blog/category', BlogCategoryAPIView.as_view()),
    path('blog/category/<int:pk>', BlogCategoryDetailAPIView.as_view()),
    path('post/comment', PostCommentCreateView.as_view()),
    path('post/mediafile', PostMediafileCreateView.as_view()),
    path('post/like', FavoritePostsViewSet),
    path('post/like/<int:pk>', FavoritePostsDetailViewSet),

]

router = routers.DefaultRouter()
router.register('blogs', BlogViewSet, base_name='api')
router.register('posts', PostViewSet, base_name='api')


urlpatterns += router.urls