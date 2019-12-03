from django.contrib import admin
from api.models import Blog, BlogCategory, Post, PostComment, PostFile, FavoritePost


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'creator')


admin.site.register(BlogCategory)
admin.site.register(PostComment)
admin.site.register(PostFile)
admin.site.register(FavoritePost)