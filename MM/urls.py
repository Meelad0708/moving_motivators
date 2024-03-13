from django.urls import path
from .views import HomeView, TeamDetailView, MemberDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team_detail'),
    path('member/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
]
