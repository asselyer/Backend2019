# Generated by Django 2.2.3 on 2019-12-03 22:29

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('body', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(default='')),
                ('types', models.PositiveIntegerField(choices=[(1, 'PUBLIC'), (2, 'PRIVATE')], default=1)),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
            managers=[
                ('public_blogs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_cat', models.PositiveIntegerField(choices=[(1, 'MUSIC'), (2, 'LIFE STYLE')], default=2)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
            managers=[
                ('music_blogs', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='FavoritePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediafile', models.FileField(blank=True, null=True, upload_to=utils.upload.post_mediafile_path, validators=[utils.validators.validate_file_size, utils.validators.validate_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('basepost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.BasePost')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'db_table': 'my_posts',
                'ordering': ('title', 'created_at'),
            },
            bases=('api.basepost',),
        ),
    ]