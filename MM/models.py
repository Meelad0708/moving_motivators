from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_leader = models.CharField(max_length=50)
    job_description = models.CharField(max_length=1000)
    # add logo


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')


class MovingMotivator(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=1000)
    # add picture


class MemberMotivator(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='motivators')
    moving_motivator = models.ForeignKey(MovingMotivator, on_delete=models.CASCADE)
    order = models.IntegerField()
    # ensure that there are no duplicate of moving motivator for a member
    # and that motivators appear in order that members have defined
    class Meta:
        unique_together = ('member', 'moving_motivator')
        ordering = ['order']



