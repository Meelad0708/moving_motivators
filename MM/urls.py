from django.urls import path
from .views import HomeView, TeamLeaderView, MemberDetailView, MemberMotivatorUpdateOrCreateView, TeamDetailView, MotivatorChangeHistoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('team-leader/', TeamLeaderView.as_view(), name='team_leader_view'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('motivators/', MemberMotivatorUpdateOrCreateView.as_view(), name='team_member_view'),
    path('member/<int:pk>/change-history/', MotivatorChangeHistoryView.as_view(), name='motivator_change_history')
]
# member/<int:pk>/<int:fk>
