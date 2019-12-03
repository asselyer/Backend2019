from django.db import models
from users.models import MainUser

from api.constants import BLOG_CATEGORIES, BLOG_TYPES, BLOG_PUBLIC, BLOG_PRIVATE, CATEG_LIFESTYLE
from utils.upload import post_mediafile_path
from utils.validators import validate_extension, validate_file_size


class CategoryMusicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(blog_cat=CATEG_MUSIC)

    def music_blogs(self):
        return self.filter(blog_cat=CATEG_MUSIC)

    def filter_by_category(self, blog_cat):
        return self.filter(blog_cat=blog_cat)


class CatLifeStyleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(blog_cat=CATEG_LIFESTYLE)

    def lifestyle_blogs(self):
        return self.filter(blog_cat=CATEG_LIFESTYLE)

    def filter_by_category(self, status):
        return self.filter(blog_cat=blog_cat)

class BlogCategory(models.Model):
    blog_cat = models.PositiveIntegerField(choices=BLOG_CATEGORIES, default=CATEG_LIFESTYLE)
    music_blogs = CategoryMusicManager()
    lifestyle_blogs = CatLifeStyleManager()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.blog_cat

    @property
    def blogs_count(self):
        return self.blogs.count()


class BlogPrivateManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(types=BLOG_PRIVATE)

    def private_blogs(self):
        return self.filter(types=BLOG_PRIVATE)

    def filter_by_block_type(self, types):
        return self.filter(types=types)


class BlogPublicManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(types=BLOG_PUBLIC)

    def public_blogs(self):
        return self.filter(types=BLOG_PUBLIC)

    def filter_by_block_type(self, types):
        return self.filter(types=types)


class Blog(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default='')
    types = models.PositiveIntegerField(choices=BLOG_TYPES, default=BLOG_PUBLIC)
    category = models.ForeignKey(BlogCategory, null=True,related_name='blogs', on_delete=models.CASCADE)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_blogs')
    public_blogs = BlogPrivateManager()
    private_blogs = BlogPublicManager()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return '{}: {}'.format(self.id, self.name, self.types, self.category, self.desc)
    
    @property
    def posts_count(self):
        return self.posts.count()

class BasePost(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    body = models.TextField(default='')

    def __str__(self):
        return '{}: {}'.format(self.id,self.title)

class Post(BasePost):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, related_name='posts', null=True)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ('title', 'created_at',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'my_posts'

    def __str__(self):
        return self.title

    @property
    def comments_count(self):
        return self.post_comments.count()

    @property
    def likes_count(self):
        return self.likes.count()
        
class PostFile(models.Model):
    mediafile = models.FileField(upload_to=post_mediafile_path, validators=[validate_file_size, validate_extension], blank=True, null=True)
    posts = models.ForeignKey(Post, null=True, related_name='post_documents', on_delete=models.CASCADE)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.id,self.mediafile)

class PostComment(models.Model):
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    posts = models.ForeignKey(Post, null=True,  related_name='post_comments', on_delete=models.CASCADE)
   
    def __str__(self):
        return '{}: {}'.format(self.id, self.body, self.created_at)
        
class FavoritePost(models.Model):
    posts = models.ForeignKey(Post, null=True,  related_name='likes', on_delete=models.CASCADE)
    users = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}: {}'.format(self.id, self.users)



