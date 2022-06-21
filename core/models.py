from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UUIDMixin(models.Model):
    class Meta:
        abstract = True


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profile_img = models.ImageField(upload_to='profile_images/', default='default-profile.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

