from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Team, Member, MemberMotivator, MovingMotivator, MotivatorChangeLog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .forms import MemberMotivatorForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    def get(self, request, *args, **kwargs):
        if request.user.member.is_team_leader:
            return redirect('team_leader_view')
        else:
            return redirect('team_member_view')

class TeamLeaderView(LoginRequiredMixin, ListView):
    model = Team
    template_name = 'MM/home.html'
    context_object_name = 'teams'

    def get_queryset(self):
        queryset = Team.objects.filter(team_leader=self.request.user.member)
        print(queryset)
        return queryset


class TeamDetailView(DetailView):
    model = Team
    template_name = 'MM/team_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.get_object()
        context['members'] = team.members.all()
        return context


class MemberDetailView(DetailView):
    model = Member
    template_name = 'MM/member_detail.html'
    context_object_name = 'member'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['motivators'] = MemberMotivator.objects.filter(member=self.object).order_by('order')
        return context

class MemberMotivatorUpdateOrCreateView(LoginRequiredMixin, FormView):
    template_name = 'MM/member_motivator_form.html'
    form_class = MemberMotivatorForm

    def form_valid(self, form):
        member = self.request.user.member
        moving_motivator = form.cleaned_data['moving_motivator']
        order = form.cleaned_data['order']

        motivator, created = MemberMotivator.objects.update_or_create(
            member=member,
            moving_motivator=moving_motivator,
            defaults={'order': order}
        )

        if not created:
            MotivatorChangeLog.objects.create(
                member_motivator=motivator,
                previous_order=motivator.order,
                new_order=order,
            )

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('member_detail', kwargs={'pk': self.request.user.member.pk})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        moving_motivator = MovingMotivator.objects.all()
        context['moving_motivator'] = moving_motivator
        return context


class MotivatorChangeHistoryView(ListView):
    model = MotivatorChangeLog
    template_name = 'MM/motivator_change_history.html'
    context_object_name = 'change_logs'

    def get_queryset(self):
        return MotivatorChangeLog.objects.filter(member_motivator__member_id=self.kwargs['pk']).select_related('member_motivator').order_by('-change_date')



# dragable for motivators