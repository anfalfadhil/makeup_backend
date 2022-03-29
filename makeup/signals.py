from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Post
from guardian.shortcuts import assign_perm


@receiver(post_save, sender=User)
def creat_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(post_save, sender=Post)
# def set_permission(sender, instance, **kwargs):
#     assign_perm(
#         "update_post",  
#         instance.user,  
#         instance  
#     )

# source : https://www.youtube.com/watch?v=FdVuKt_iuSI&t=15s