from django.contrib import admin
from .models import *
# Register your models here.

'''@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','profile_pic', 'bio', 'cover')
    list_display_links= ('id','profile_pic')
    list_editable=('cover',)
    search_fields= ('bio')
    list_per_page=20
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','creater', 'date_created', 'content_text','content_image','likers','savers','comment_count')
    list_display_links= ('id','creater')
    list_filter= ('creater',)
    list_editable=('content_image',)
    search_fields= ('creater')
    list_per_page=20
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('id','post', 'commenter', 'comment_content','comment_time')
    list_display_links= ('id','commenter')
    list_filter= ('commenter',)
    list_editable=('comment_content',)
    search_fields= ('commenter')
    list_per_page=20
    
@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display=('id','user', 'follower')
    list_display_links= ('id','user')
    list_filter= ('follower',)
    list_editable=('follower',)
    search_fields= ('follower')
    list_per_page=20'''
    
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Follower)
