from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Moving_Motivators(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=1000)


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    member = models.ManyToManyField(User, through='Member')

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    moving_motivators = models.ManyToManyField(Moving_Motivators)


