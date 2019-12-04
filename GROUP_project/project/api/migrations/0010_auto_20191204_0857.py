# Generated by Django 2.2.3 on 2019-12-04 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20191204_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='blogs',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='api.BlogCategory'),
        ),
    ]