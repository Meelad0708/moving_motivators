from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_leader = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True, blank=True, related_name='leads_team') # foreign key to memeber
    project_description = models.CharField(max_length=1000)
    # add logo

    def __str__(self):
        return self.team_name


class Member(models.Model): # add more fields such as email, team leader boolean
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='members')
    is_team_leader = models.BooleanField(default=False)
    # add picture of employee

    def __str__(self):
        return self.user.get_full_name() or self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Member.objects.create(user=instance)
    instance.member.save()


class MovingMotivator(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=1000)
    # add picture

    def __str__(self):
        return self.name

class MemberMotivator(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='motivators')
    moving_motivator = models.ForeignKey(MovingMotivator, on_delete=models.CASCADE)
    order = models.IntegerField()
    date = models.DateField(auto_now=True)
    # ensure that there are no duplicate of moving motivator for a member
    # and that motivators appear in order that members have defined
    class Meta:
        unique_together = ('member', 'moving_motivator')
        ordering = ['order']

    def __str__(self):
        return f"{self.member.user.username} - {self.moving_motivator.name}"


class MotivatorChangeLog(models.Model):
    member_motivator = models.ForeignKey(MemberMotivator, on_delete=models.CASCADE, related_name='change_logs')
    previous_order = models.IntegerField(null=True, blank=True)
    new_order = models.IntegerField(null=True, blank=True)
    change_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-change_date']


# create similar table for team member
