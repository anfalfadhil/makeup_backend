from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path("", views.HomePage.as_view(), name= "home-page"),
    path("posts", views.Posts.as_view(), name="all-posts"),
    path("posts/<slug:slug>", views.SinglPost.as_view(), name= "single_post"),
    path("add_to_my_palette", views.AddToMyPalette.as_view(), name="add_to_my_palette"),
    # path("register", views.Register, name="register"),
    path("register", views.register_request, name="register"),
    path("login", views.Login, name="login"),
    path("logout", views.Logout, name="logout"),
    path("new-post", views.CreatePost, name="new-post"),
    path("update-post/<str:pk>", views.UpdatePost, name="update-post"),
    path("delete-post/<str:pk>", views.DeletePost, name="delete-post"),
    path("user", views.userProfile, name="user-profile"),
    path("edit-profile", views.profileEdit, name="edit-profile"),
    path("like/<slug:slug>", views.LikeFunc, name="like-post"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

