# Generated by Django 2.2.3 on 2019-09-25 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190925_0904'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectmember',
            old_name='project_members',
            new_name='projects',
        ),
    ]
