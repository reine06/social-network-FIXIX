from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("index/", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("profile/<str:username>", views.profile, name='profile'),
    path("following/", views.following, name='following'),
    path("saved/", views.saved, name="saved"),
    path("createpost/", views.create_post, name="createpost"),
    path("follow/<str:username>", views.follow, name="followuser"),
    path("unfollow/<str:username>", views.unfollow, name="unfollowuser"),
    path("post/<int:post_id>/edit", views.edit_post, name="editpost"),
    path("post/<int:id>/like", views.like_post, name="likepost"),
    path("post/<int:id>/unlike", views.unlike_post, name="unlikepost"),
    path("post/<int:post_id>/delete", views.delete_post, name="deletepost"),
    path("post/<int:id>/save", views.save_post, name="savepost"),
    path("post/<int:id>/unsave", views.unsave_post, name="unsavepost"),
    path("post/<int:post_id>/comments", views.comment, name="comments"),
    path("post/<int:post_id>/write_comment",views.comment, name="writecomment"),
    path('elearning/',views.elearning, name='elearning'),
    path('profile/edit_profile', views.editprofile, name='editprofile'),

    
    path('inbox/',views.inbox,name='inbox'),
    path('inbox/create-thread/', views.createthread, name='create-thread'),
    path('inbox/<int:pk>/', views.thread, name='thread'),
    path('inboxf/<int:receiver_id>/', views.threadfollower, name='threadf'),
    path('inbox/<int:receiver_id>/create-message/', views.createmessage, name='create-message'),
    path("inbox/<int:id>/delete", views.delete_thread, name="deletethread"),

   
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password_reset_done.html"), name ='password_reset_complete')
]

