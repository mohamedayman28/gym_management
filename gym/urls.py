
from django.urls import path
# Local apps
from gym import views


urlpatterns = [
    # Local apps
    path('', views.HomePageView.as_view(), name='home_page'),
    path('member/form/', views.MemberFormView.as_view(), name='member_form'),
    path('member/add/', views.MemberAddView.as_view(), name='member_add'),
    path('login/', views.LogInView.as_view(), name='login_page'),
]
