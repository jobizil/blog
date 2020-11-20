from django.db import models
from django.contrib.auth.models import User

# Extend a 1-1 relationship model with existing blog model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}\'s Profile'
