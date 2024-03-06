from django.contrib import admin
from .models import MovingMotivator, Team, Member, MemberMotivator
# Register your models here.

admin.site.register(MovingMotivator)
admin.site.register(Team)
admin.site.register(Member)
admin.site.register(MemberMotivator)