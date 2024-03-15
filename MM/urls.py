from django.urls import path
from .views import HomeView, TeamLeaderView, MemberDetailView, MemberMotivatorUpdateOrCreateView, TeamDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('team-leader/', TeamLeaderView.as_view(), name='team_leader_view'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('motivators/', MemberMotivatorUpdateOrCreateView.as_view(), name='team_member_view'),
]
