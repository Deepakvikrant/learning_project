from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    #additionall

    portfolio_site = models.URLField(blank = True)

    portfolio_pic =models.ImageField(upload_to ='profile_pic',blank= True)

    def __self__(self):
        return self.user.username
