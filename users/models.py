from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Extend a 1-1 relationship model with existing blog model


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    # Override default save method
    def save(self):
        """ Use PIL Library
         First run save method of parent class"""
        super().save()
        # Open Image instance
        img = Image.open(self.image.path)

        # Check Image size
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
