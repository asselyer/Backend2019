from django.contrib import admin
from api.models import Article, FavoriteArticle

admin.site.register(Article)
admin.site.register(FavoriteArticle)