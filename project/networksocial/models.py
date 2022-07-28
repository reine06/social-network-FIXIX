
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pic/')
    bio = models.TextField(max_length=200,blank=True,null=True)
    cover= models.ImageField(upload_to ='covers/',blank=True)
    # follower = models.ManyToManyField("self",blank=True,related_name='following')
    
    
    def  __str__(self):
        return self.username
    
    @property
    def full_name(self):
        return f' {self.username.first_name} {self.username.last_name}'
    
    @property
    def posts_list(self):
        return self.username.posts.filter(author=self.username)
    
    @property
    def comments_list(self):
        return self.username.comments.filter(author=self.username)
    
        
   
 
        

class Post(models.Model):
    creater = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    date_created = models.DateTimeField(default = timezone.now)
    content_text = models.TextField(max_length=200,blank=True)
    content_image = models.ImageField(upload_to='posts/',blank= True)
    likers = models.ManyToManyField(User,blank=True, related_name = 'likes')
    savers = models.ManyToManyField(User,blank=True,related_name='saved')
    comment_count= models.IntegerField(default=0)
    
    def __str__(self) :
        return f"Post ID: {self.id} (created: {self.creater} ) "
    


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    commenter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='commenters')
    comment_content = models.TextField(max_length=100)
    comment_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self) :
        return f"Post : {self.post} | Commenter: {self.commenter} "
    
# class Follower(models.Model):
#     follower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='followers',null=True)
#     following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following',null=True)
  
    
#     def __str__(self) :
#         return f'Follower : {self.following} '
    
class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers',null=True)
    followers = models.ManyToManyField(User, blank=True, related_name='following')

    def __str__(self):
        return f"User: {self.user}"



class ThreadModel(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')

class MessageModel(models.Model):
	thread = models.ForeignKey(ThreadModel, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
	sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
	body = models.CharField(max_length=1000)
	image = models.ImageField(upload_to='uploads/message_photos', blank=True, null=True)
	date = models.DateTimeField(default=timezone.now)
	is_read = models.BooleanField(default=False)
         
         
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     