from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth#module de django
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json

# Create your views here.

def index(request):
   all_posts= Post.objects.order_by('-date_created')
   paginator = Paginator(all_posts,5)#5 posts par page
   page_number = request.GET.get('page')#page recupere et mets ces donnees
   if page_number == None:#desactiver la pagination
      page_number = 1
   posts = paginator.get_page(page_number)
   # postDesPersonnesQueJeSuis = []
   # if request.user.is_authenticated:
   #    # followings =Follower.objects.filter(following=request.user)
   #    followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
   followings = []
   suggestions = []
   if request.user.is_authenticated:
      followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
      suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]
   return render(request, 'network/index.html', {
        "posts": posts,
        "suggestions": suggestions,
        "page": "all_posts",
        'profile': False
    })
      # for f in followings:
      #    postDesPersonnesQueJeSuis.append(f.follower.posts_list)
   # return render(request, 'index.html', { 'postoffollowings': postDesPersonnesQueJeSuis, 'posts':posts })

def login_view(request):
   if request.method == 'POST':
         username= request.POST['username']
         password= request.POST['password']
        
         user = auth.authenticate(username=username, password=password)
         if user is not None:
               auth.login(request,user)
               messages.success(request, 'you are now logged in!')
               return redirect('index')
         else:
            messages.error(request, 'INVALID username and/or password , try again...')
            return redirect('login')
   
   return render(request, 'network/login.html')
   

def logout_view(request):
    logout(request)
    return redirect("index")


def register(request):
   if request.method == "POST":
         username = request.POST["username"]
         email = request.POST["email"]
         fname = request.POST["firstname"]
         lname = request.POST["lastname"]
         profile = request.FILES.get("profile")
         print(f"Profile: {profile}")
         cover = request.FILES.get('cover')
         print(f"Cover: {cover}")

         # confirmation du mot de passe
         password = request.POST["password"]
         confirmation = request.POST["confirmation"]
         if password != confirmation:
            messages.error(request, 'Passwords must match, try again...')
            return redirect( "register")
            # check username
         else: 
            if User.objects.filter(username=username).exists():
               messages.error(request, 'That username is taken')
               return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
              # creation de nouvel utilisateur
                  user = User.objects.create(username=username,email=email, first_name = fname, last_name = lname)
                  user.set_password(password)
                  user.profile_pic = profile
                  user.cover = cover
                  '''else:
                     user.profile_pic = "profile_pic/no_pic.png"
                     user.cover = cover '''          
                  user.save() 
                  return redirect('login')
   
   return render(request, "network/register.html")

'''@login_required
def profile(request, username):
   user = User.objects.get(username=username)
   all_posts = Post.objects.filter(creater=user).order_by('-creater')
   paginator = Paginator(all_posts, 5)
   page_number = request.GET.get('page')
   if page_number == None:
      page_number = 1
   posts = paginator.get_page(page_number)
    #  pour trouver les abonnees
   followers = Follower.objects.filter(following=user)
   this_user_follow=False
   for obj in followers:
         if request.user == obj.follower:
            this_user_follow= True
   followers_count = followers.count()
     #  pour trouver lees abonnements
   followings = Follower.objects.filter(follower=user)
   this_user_following=False
   for obj in followings:
         if request.user == obj.follower:
            this_user_following= True
   followings_count = followings.count()
   
  
   return render(request, 'accounts/profile.html', {
         "username": user,
         "posts": posts,
         "following" : followings,
         "follower": followers,
         "followers_count":followers_count,
         "followings_count": followings_count,
         'flag':this_user_follow,
        'flags':this_user_following,
     })'''

def profile(request, username):
    user = User.objects.get(username=username)
    all_posts = Post.objects.filter(creater=user).order_by('-date_created')
    paginator = Paginator(all_posts, 5)
    page_number = request.GET.get('page')
    if page_number == None:
        page_number = 1
    posts = paginator.get_page(page_number)
    followings = []
    suggestions = []
    follower = False
    if request.user.is_authenticated:
        followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
        suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]

        if request.user in Follower.objects.filter(user=user):
            follower = True
    #  pour trouver les abonnees
    follower_count = Follower.objects.filter(user=user).count()  
    #  pour trouver lees abonnements
    following_count = Follower.objects.filter(followers=user).count()
    return render(request, 'network/profile.html', {
        "username": user,
        "posts": posts,
        "posts_count": all_posts.count(),
        "suggestions": suggestions,
        "page": "profile",
        "is_follower": follower,
        "follower_count": follower_count,
        "following_count": following_count
    })

@login_required
def follow(request, username):
   if request.user.is_authenticated:
      user = User.objects.get(username=username)
      follower=Follower.objects.create(user=user)
      print(f"User: {user}")
      print(f"Follower: {request.user}")
      follower.followers.add(request.user)
      follower.save()
      return redirect('profile', username=username)

   else :
       return redirect('login')


@csrf_exempt
def unfollow(request, username):
   if request.user.is_authenticated:
         if request.method == 'PUT':
            user = User.objects.get(username=username)
            print(f"User: {user}")
            print(f"Unfollower: {request.user}")
            follower = Follower.objects.get(user=user)
            follower.followers.remove(request.user)
            follower.save()
         return redirect('profile', username=username)

   else :
       return redirect('login')

 
@login_required
def following(request):
   if request.user.is_authenticated:
      following_user = Follower.objects.filter(followers=request.user).values('user')
      all_posts = Post.objects.filter(creater__in=following_user).order_by('-date_created')
      paginator = Paginator(all_posts,5)
      page_number =request.GET.get('page')
      if page_number == None:
         page_number = 1
      posts = paginator.get_page(page_number)
      followings = Follower.objects.filter(followers=request.user).values_list('user', flat=True)
      suggestions = User.objects.exclude(pk__in=followings).exclude(username=request.user.username).order_by("?")[:6]

      return render(request, 'network/index.html', { "posts":posts,"page":followings,"suggestions": suggestions } )
   else:
       return redirect('login')






@login_required  
def saved(request):
   if request.user.is_authenticated:
      all_posts = Post.objects.filter(savers=request.user).order_by('date_created')
      paginator = Paginator(all_posts,5)
      page_number =request.GET.get('page')
      if page_number == None:
         page_number = 1
      posts = paginator.get_page(page_number)
      Follower.objects.filter(followers=request.user)
      return render(request,'network/index.html', { "posts":posts,"page":"saved" })
   else:
      return redirect('login')
        

      
@login_required
def create_post(request):
   if request.method == 'POST':
      text = request.POST.get('text')
      pic =request.FILES.get('picture')
      Post.objects.create(creater=request.user, content_text=text,content_image=pic)
   return redirect('index')

@login_required
@csrf_exempt
def like_post(request,id):
   if request.user.is_authenticated:
      post = Post.objects.get(pk=id)
      post.likers.add(request.user)
      post.save()
   return redirect('index')
  
@login_required
@csrf_exempt
def unlike_post(request,id):
   if request.user.is_authenticated:
      post = Post.objects.get(pk=id)
      post.likers.remove(request.user)
      post.save()
   return redirect('index')

@login_required
@csrf_exempt
def save_post(request,id):
   if request.user.is_authenticated:
      post = Post.objects.get(pk=id)
      post.savers.add(request.user)
      post.save()
   return redirect('index')

@csrf_exempt
def unsave_post(request,id):
   if request.user.is_authenticated:
      post = Post.objects.get(pk=id)
      post.savers.remove(request.user)
      post.save()
   return redirect('index')

@csrf_exempt
def delete_post(request,post_id):
   if request.user.is_authenticated:
      post = Post.objects.get(id=post_id)
      if request.user == post.creater :
         post.delete()
   return redirect('index')
   
@csrf_exempt
def comment(request,post_id):
   if request.user.is_authenticated:
      if request.method == 'POST':
         comment_texte = request.POST.get('comment')
         post = Post.objects.get(id=post_id)
         newcomment = Comment.objects.create(post=post,commenter=request.user,comment_content=comment_texte)
         post.comment_count += 1
         post.save()
         return redirect('index')


@login_required
@csrf_exempt
def edit_post(request,post_id):
   if request.method == 'POST':
      text = request.POST.get('text')
      pic = request.FILES.get('picture')
      # img_chg = request.get('img_change')
      post = Post.objects.get(id=post_id)
      post.content_text =text
      if pic:
         post.content_image = pic
         post_text = post.content_text 
         post.save()
