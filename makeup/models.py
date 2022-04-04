from django.template.defaultfilters import slugify
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save 


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=500)
    image=models.ImageField(upload_to='blog_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="posts")
    date = models.DateTimeField(auto_now=True)
    content= models.TextField(blank=True)
    slug= models.SlugField(default="", max_length=20, blank=True, null=False, db_index=True, unique=True)
    tags = models.ManyToManyField('Tag')
    likes = models.ManyToManyField(User, related_name="bposts")

    

    def total_likes(self):
        return self.likes.count()


    # def save(self, *args, **kwargs):
    #     self.slug= slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()




class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Comments(models.Model):
    comment= models.TextField(max_length=1000, null=True)
    post= models.ForeignKey(Post, on_delete=CASCADE, related_name="comments", null=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default="default.jpg", upload_to='blog_images')
    posts = models.ManyToManyField(Post)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    date_joined= models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
	    if created:
		    Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance, *args, **kwargs):
	    instance.profile.save(*args, **kwargs)


        

    
