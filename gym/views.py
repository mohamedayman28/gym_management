# Django
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
# Local apps
from gym.forms import MemberForm
from gym.models import Member


class HomePageView(ListView):
    template_name = 'index.html'
    model = Member
    context_object_name = 'members'


class MemberFormView(LoginRequiredMixin, CreateView):
    # Redirect unauthenticated user.
    login_url = reverse_lazy('gym:login')
    template_name = 'member_form.html'
    form_class = MemberForm
    # Redirect after submit form valid.
    success_url = reverse_lazy('gym:index')


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    # Redirect unauthenticated user.
    login_url = reverse_lazy('gym:login')
    model = Member
    template_name_field = 'member'
    # Redirect after successful delete.
    success_url = reverse_lazy('gym:index')


class MemberUpdateView(LoginRequiredMixin, UpdateView):
    # Redirect unauthenticated user.
    login_url = reverse_lazy('gym:login')
    template_name = 'member_form.html'
    form_class = MemberForm
    model = Member
    # Redirect after submit form valid.
    success_url = reverse_lazy('gym:index')


class LoginView(views.LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True


class LogoutView(views.LogoutView):
    template_name = 'logged_out.html'
