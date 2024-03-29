# Generated by Django 2.2.3 on 2019-12-03 08:57

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
            name='BaseTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('block_type', models.PositiveIntegerField(choices=[(1, 'DONE'), (2, 'TODO'), (3, 'IN PROGRESS'), (4, 'CODE REVIEW')], default=2)),
            ],
            managers=[
                ('done_blocks', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('desc', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(blank=True, null=True, upload_to=utils.upload.task_document_path, validators=[utils.validators.validate_file_size, utils.validators.validate_extension])),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('basetask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.BaseTask')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'DONE'), (2, 'TODO'), (3, 'TESTED')], default=2)),
                ('is_deleted', models.BooleanField(default=False)),
                ('priority', models.PositiveIntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')], default=2)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
                'db_table': 'my_tasks',
                'ordering': ('name', 'status'),
            },
            bases=('api.basetask',),
        ),
    ]
