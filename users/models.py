from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    '''Stores logged in user's information'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __self__(self):
        return f'Profil {self.user.username}'

