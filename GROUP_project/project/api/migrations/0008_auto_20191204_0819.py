# Generated by Django 2.2.3 on 2019-12-04 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191204_0704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcategory',
            old_name='blog_cat',
            new_name='blog_category',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='categories',
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='blogs',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='api.Blog'),
        ),
    ]
