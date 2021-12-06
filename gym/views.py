# Django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View, generic
# Local apps
from gym.forms import MemberForm
from gym.models import Member


class HomePageView(generic.TemplateView):
    template_name = 'home_page.html'
    extra_context = {'members': Member.objects.all()}


class MemberFormView(generic.TemplateView):
    template_name = 'member_form.html'
    extra_context = {'form': MemberForm()}


class MemberAddView(View):
    def post(self, request):
        if request.user.is_authenticated:

            form = MemberForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home_page')
            else:
                return render(request, 'member_form.html', {'form': form})

        elif not request.user.is_authenticated:
            return redirect('login_page')


class LogInView(View):
    def get(self, request):
        return HttpResponse('Allowed!!')
