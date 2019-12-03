from django.db import models
from users.models import MainUser

from api.constants import ARTICLE_COLORS, ARTICLE_COLORS_RED
from utils.upload import article_image_path
from utils.validators import validate_extension, validate_file_size


class Article(models.Model):
    name = models.CharField(max_length=300)
    desc = models.TextField()
    price = models.IntegerField()
    city = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    color = models.PositiveIntegerField(choices=ARTICLE_COLORS, default=ARTICLE_COLORS_RED)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_articles')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.name

    @property
    def favorite_articles_count(self):
        return self.favorite_articles.count()

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name='article_images', null=True)
    image = models.ImageField(upload_to=article_image_path, validators=[validate_file_size, validate_extension], blank=True, null=True)

    def __str__(self):
        return self.article


class FavoriteArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name='favorite_articles', null=True)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='liked_articles')

    class Meta:
        verbose_name = 'Fav_artic'
        verbose_name_plural = 'Fav_artics'
        db_table = 'my_favorites'

    def __str__(self):
        return self.user.id
