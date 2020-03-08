from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    profile_user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_age = models.IntegerField(default=0)
    profile_credits = models.IntegerField(default=0)
