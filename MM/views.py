from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Team, Member, MemberMotivator

# Create your views here.


class HomeView(ListView):
    model = Team
    template_name = 'MM/home.html'
    context_object_name = 'teams'

class TeamDetailView(DetailView):
    model = Team
    template_name = 'MM/team_detail.html'
    context_object_name = 'team'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'MM/member_detail.html'
    context_object_name = 'member'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motivators'] = MemberMotivator.objects.filter(member=self.object).order_by('order')
        return context
