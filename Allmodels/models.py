from pstats import Stats
from sre_parse import CATEGORIES
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class PostModel (models.Model):
    Categories =(
        ("BEGINNER","BEGINNER"),
        ("INTERMEDIATE","INTERMEDIATE"),
        ("ADVANCE","ADVANCE"),
        ("MASTERCLASS","MASTERCLASS")
    )
    Title = models.CharField(max_length=150)
    Description= models.TextField()
    Link = models.CharField(max_length=255)
    Level =models.CharField(choices=Categories,default="BEGINNER",max_length=50)
    No_of_videos =  models.CharField(max_length=50)
    Created_By = models.ForeignKey(User, on_delete=models.CASCADE)
    Status = models.BooleanField(default=True)
    created_At = models.DateField( auto_now_add=True)
    Updated_At = models.DateField(  auto_now_add=True)

    def __str__(self) -> str:
        return self.Title

class Comment(models.Model):
    Commented_By = models.ForeignKey(User, on_delete=models.CASCADE)   
    Post = models.ForeignKey(PostModel,related_name="comments", on_delete=models.CASCADE)
    created_At = models.DateField( auto_now_add=True)
    Content  = models.TextField()
    def __str__(self) -> str:
        return self.Content

class Profile(models.Model):
    profile_user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile/",default ="null")
    bio = models.TextField(blank=True,default ="null")
    interest = models.TextField(blank=True,default ="null")
    created = models.DateTimeField(auto_now=False, auto_now_add=True,blank=True)


    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(profile_user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.profile_user.username