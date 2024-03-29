# Generated by Django 2.2.3 on 2019-12-03 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191203_1457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmember',
            old_name='projects',
            new_name='project',
        ),
        migrations.RemoveField(
            model_name='block',
            name='block_type',
        ),
        migrations.AddField(
            model_name='block',
            name='projects',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='api.Project'),
        ),
        migrations.AlterField(
            model_name='block',
            name='types',
            field=models.PositiveIntegerField(choices=[(1, 'DONE'), (2, 'TODO'), (3, 'IN PROGRESS'), (4, 'CODE REVIEW')], default=2),
        ),
    ]
