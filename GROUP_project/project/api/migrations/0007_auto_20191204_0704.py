# Generated by Django 2.2.3 on 2019-12-04 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191204_0703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category',
            new_name='categories',
        ),
    ]
