from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    # objects = None
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,  null=True)
    image = models.ImageField(default='media/profile_pics/profile.jpg', upload_to='profile_pics')
    # https://darrenproject4.s3-eu-west-1.amazonaws.com/media/profile_pics/profile.jpg

    def __str__(self):
        return self.user.username

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)






