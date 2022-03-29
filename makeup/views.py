from typing import Mapping
from django.shortcuts import redirect, render
from django.views import generic
from django.views.generic import ListView, DeleteView, CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from makeup.decorators import unAllowed_user, allowed_users
from .models import  Post, Author, Profile
from .form import CommentForm, RegisterForm, NewPostForm, UserUpdateForm, ProfileUpdateForm
from django.views import View
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from makeup import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User, BaseUserManager
from django.contrib.auth.decorators import permission_required
from rest_framework.permissions import SAFE_METHODS, DjangoModelPermissions, IsAdminUser, BasePermission
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .form import NewPostForm, NewUserForm



class PostUserWritePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user




class HomePage(ListView) :
    template_name = "makeup/index.html"
    model = Post


# @login_required(login_url='login')
# @allowed_users(allowed_actions=["admin"])
class Posts(ListView):
    template_name = "makeup/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name= "posts"
    def get_queryset(self) :
        posts =  super().get_queryset()
        return posts


class SinglPost(View):

    def checkInMyPalette(self, request, post_id):
            posts_in_palette = request.session.get("myPalette")
            if posts_in_palette is not None:
                is_in_my_palette = post_id in posts_in_palette
            else:
                is_in_my_palette = False
            return is_in_my_palette

    def get(self, request, slug, *args, **kwargs):
        post = Post.objects.get(slug=slug)

        total_likes= post.total_likes()
        context = {
            "total_likes": total_likes,
            "post" : post,
            "tags" : post.tags.all(),
            "comment_form" : CommentForm,
            "comments": post.comments.all().order_by("-id"),
            "in_my_palette": self.checkInMyPalette(request, post.id)
        }
        return render (request, "makeup/single_post.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.name = User.objects.get(pk=request.user.id) 
            comment.save()

            return HttpResponseRedirect(reverse("single_post", args=[slug]))
        context = {
            "post" : post,
            "tags" : post.tags.all(),
            "comment_form" : CommentForm,
            "comments": post.comments.all().order_by("-id"),
            "in_my_palette": self.is_in_my_palette(request, post.id)
        }
        return render (request, "makeup/single_post.html", context)



class AddToMyPalette(View):
    def get(self, request):
        myPalette = request.session.get("myPalette")
        context = {}
        if myPalette is None or len(myPalette) == 0 :
            context["posts"] = []
            context["has_posts"] = False
        else :
            my_posts = Post.objects.filter(id__in=myPalette)
            context["posts"] = my_posts
            context["has_posts"] = True
        return render(request, "makeup/my_palette.html", context)

    def post(self, request ):
        myPalette = request.session.get("myPalette")
        post_id = int(request.POST["post_id"])
        if myPalette is None:
            myPalette = [] 
        if post_id not in myPalette :
            myPalette.append(post_id)
        else:
            myPalette.remove(post_id)
        request.session["myPalette"] = myPalette
        return HttpResponseRedirect("add_to_my_palette")





def register_request(request):
    
    if request.method== 'POST' :
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        email= request.POST['email']

        if password1 == password2 :
                if User.objects.filter(email=email).exists():
                    print('Email is already exists')
                    messages.info(request, "Email address already exists")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username= username, password=password1, email=email, first_name= first_name, last_name= last_name)
                    user.save()
                    print('user created')
                    return redirect('login')

        else:
            print('password not matching')
        return redirect('register')

    else:
        return render(request, 'accounts/register.html')








@unAllowed_user
def Login(request):
    form = AuthenticationForm(data= request.POST)
    if request.method == "POST":
        username = request.POST.get('username')
        password =request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("all-posts")
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {"form":form}
    return render(request, "accounts/login.html", context)

        
def Logout(request):
    logout(request)
    return redirect("login")


def CreatePost(request):
    form = NewPostForm()
    if request.method == "POST" :
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False) 
            obj.author = User.objects.get(pk=request.user.id) 
            obj.save()
            return redirect('all-posts')
    context={"form" : form}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return form.form_valid()

    
    return render(request, "posts/create.html", context)






class UserAdmin(BaseUserManager):
    ...
    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser







def UpdatePost(request, pk):
    post= Post.objects.get(id=pk)
    form = NewPostForm(instance=post)
    if request.method == "POST" and request.user.has_perm("makeup.update_post") :
        form = NewPostForm(request.POST, instance=post )
        if form.is_valid():
            form.save()
            return redirect('all-posts')
    context = {"form" : form}


    return render(request, "posts/create.html", context)


def DeletePost(request, pk):
    post= Post.objects.get(id=pk)
    if request.method =="POST":
        post.delete()
        return redirect('all-posts')
    context={"post": post}
    return render(request, "posts/delete.html", context)

# @allowed_users(allowed_actions=['user'])
def userProfile(request):    
    posts = Post.objects.filter(author = request.user).order_by('-date')
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
    return render(request, "accounts/profile.html")



def profileEdit(request) :
    print(request.user)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
        

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Your beauty has been updated🦋")
            return redirect("user-profile")

    else:
        user_form = UserUpdateForm(instance=request.user)

        profile_form = ProfileUpdateForm(instance=request.user.profile)
        messages.MessageFailure(request, f"OOOps didn't work")
        messages.error(request, f"ooops didn't work")
          
        context = {
            "user_form": user_form,
            "profile_form" : profile_form,
        }
        return render(request, "accounts/profile-edit.html", context)


    return render(request, "accounts/profile-edit.html")

def LikeFunc(request, slug):
    print(request)
    post = Post.objects.get(slug=slug)
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse("single_post", args=[str(slug)]))