# Generated by Django 3.2.4 on 2021-06-09 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('like', '0002_auto_20210609_0424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='ingredient_id',
            new_name='ingredient',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='user_id',
            new_name='user',
        ),
    ]