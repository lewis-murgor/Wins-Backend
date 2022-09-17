from django.db import models
from django.contrib.auth.models import User

# Create your models here.

LIKE_CHOICE = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Profile (models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    Bio = models.TextField(blank=True)

class Win (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    photo_path = models.ImageField(upload_to='images/', blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    likes = models.ManyToManyField(User,blank=True,related_name='likes')
    comments = models.TextField()

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    win = models.ForeignKey(Win,on_delete=models.CASCADE)
    comment = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    win = models.ForeignKey(Win, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICE,default='Like',max_length=10)
