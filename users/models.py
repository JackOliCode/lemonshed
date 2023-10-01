from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='users', default='no_picture_user.jpg')

    def __str__(self):
        return str(self.username)