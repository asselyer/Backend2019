from api.models import ArticleImage, Article, FavoriteArticle
from rest_framework import serializers

from users.serializers import UserSerializer


class ArticleSerializer(serializers.ModelSerializer):

    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    favorite_articles_count = serializers.IntegerField(default=0, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'name', 'desc', 'price','city', 'color','creator', 'favorite_articles_count')

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return obj.creator.username


class ArticleShortSerializer(serializers.ModelSerializer):
    article_id = serializers.IntegerField(write_only=True)
    creator = UserSerializer(read_only=True)
    #document = serializers.FileField(write_only=True)
    #document_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'name','article_id',  'price', 'creator' ,'favorite_articles_count')

class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = '__all__'

class ArticleFullSerializer(ArticleShortSerializer):
    class Meta(ArticleShortSerializer.Meta):
        fields = ArticleShortSerializer.Meta.fields + ('desc', 'color')

# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ('id', 'name', 'desc','price','city', 'color', 'creator')

class ArticleFavSerializer(serializers.ModelSerializer):
    article_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = FavoriteArticle
        fields = ('article_id', 'user_id')



