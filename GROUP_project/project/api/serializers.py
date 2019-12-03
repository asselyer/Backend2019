from api.models import Blog, BlogCategory, Post, PostComment, PostFile, FavoritePost
from rest_framework import serializers

from users.serializers import UserSerializer

class BlogCategorySerializer(serializers.ModelSerializer):
    blogs_count = serializers.IntegerField(default=0, read_only=True)
    
    class Meta:
        model = BlogCategory
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(many=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    posts_count = serializers.IntegerField(default=0, read_only=True)
    
    class Meta:
        model = Blog
        fields = '__all__'

class BlogSerializer1(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    types = serializers.IntegerField()
    desc = serializers.CharField(required=False)
    category = BlogCategorySerializer(many=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def create(self, validated_data):
        blog = Blog.objects.create(**validated_data)
        return blog

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.types = validated_data.get('types', instance.types)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.category_id = validated_data.get('category_id', instance.category_id)

        instance.save()
        return instance

    def validate_types(self, value):
        if 1 < value > 2:
            raise serializers.ValidationError('types options: [1, 2]')
        return value

class PostSerializer1(serializers.ModelSerializer):

    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    body = serializers.CharField(required=True)

    class Meta:
        model = {Post}
        fields = ('id', 'title','creator', )

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tasks_count = serializers.IntegerField(default=0, read_only=True)
    title = serializers.CharField(required=False)
    body = serializers.CharField(required=True)


    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return obj.creator.username == 'Anonymus'

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post
    

class PostMediaSerializer(serializers.ModelSerializer):
    mediafile = serializers.FileField(required=False)
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostFile
        fields = ('id', 'mediafile', 'creator', 'posts')

# class TaskDocSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TaskDocument
#         fields = ['document']

class PostCommentSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = PostComment
        fields = ('id', 'body', 'creator', 'created_at','posts')


class PostShortSerializer(serializers.ModelSerializer):
    blog_id = serializers.IntegerField(write_only=True)
    creator = UserSerializer(read_only=True)

    #document = serializers.FileField(write_only=True)
    #document_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'blog_id','creator')

    # def get_document_url(self, obj):
    #     if obj.document:
    #         return self.context['request'].build_absolute_uri(obj.document.url)
    #     return None

# class SetExecutorSerializer(serializers.ModelSerializer):
#     executor = UserSerializer()
#     creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     # document = serializers.FileField(write_only=True)
#     # document_url = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Task
#         fields = ('creator', 'executor')



class PostFullSerializer(PostShortSerializer):
    post_documents = PostMediaSerializer(many=True, read_only=True, required=False)
    post_comments = PostCommentSerializer(many=True, read_only=True, required=False)

    class Meta(PostShortSerializer.Meta):
        fields = PostShortSerializer.Meta.fields + ('body', 'post_documents', 'post_comments')

class PostChangeSerializer(serializers.ModelSerializer):
    # task_comments = TaskCommentSerializer(many=True, read_only=True, required=False)
    post_documents = PostMediaSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Post
        fields = ('id', 'name', 'post_documents', 'creator')

class FavoritePostSerializer(serializers.ModelSerializer):
    posts = PostChangeSerializer()
    users = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FavoritePost
        fields = '__all__'

