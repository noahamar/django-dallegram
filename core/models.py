from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

#  Profile model
class Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  display_name = models.CharField(max_length=100, blank=True)
  profile_image = models.ImageField(upload_to='profile_images', default='profile_images/default.png')

  def __str__(self):
    return self.user.username

#  Post model
class Post(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
  image = models.ImageField(upload_to='post_images', blank=True)
  caption = models.TextField(blank=True)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.caption