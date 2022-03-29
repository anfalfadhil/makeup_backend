from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, Author, Tag, Comments, Profile
from makeup import models
# Register your models here.

class AdminPosts(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("date", "author",)
    prepopulated_fields = {"slug": ("title",)}

class AdminCommentControl (admin.ModelAdmin):
    list_display = ("comment", "post")

admin.site.register(Post, AdminPosts)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comments, AdminCommentControl)
admin.site.register(Profile),


