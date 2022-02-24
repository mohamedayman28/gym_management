# Django
from django.urls import path
# Local apps
from gym import views


app_name = 'gym'

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('member/form/', views.MemberFormView.as_view(), name='member_form'),
    path('member/<int:pk>/delete/', views.MemberDeleteView.as_view(), name='member_delete'),
    path('member/<int:pk>/update/', views.MemberUpdateView.as_view(), name='member_update'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
