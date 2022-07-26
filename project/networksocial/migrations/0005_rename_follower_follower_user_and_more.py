# Generated by Django 4.0.6 on 2022-07-17 13:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('networksocial', '0004_remove_follower_user_follower_following_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='follower',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='following',
        ),
        migrations.AddField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
