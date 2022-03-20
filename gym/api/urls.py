# Django
from django.urls import path
# Local apps
from gym.api import views

urlpatterns = [
    path('member/list/', views.MemberListAPI.as_view()),
    path('member/create/', views.MemberCreateAPI.as_view()),
    path('member/<int:pk>/delete/', views.MemberDeleteAPI.as_view()),
    path('member/<int:pk>/update/', views.MemberUpdateAPI.as_view()),
]
