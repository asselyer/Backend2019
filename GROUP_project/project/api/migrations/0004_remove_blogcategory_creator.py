# Generated by Django 2.2.3 on 2019-12-03 23:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_blogcategory_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='creator',
        ),
    ]