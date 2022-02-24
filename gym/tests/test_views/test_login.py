# Django
from django.contrib.auth import views
from django.test import TestCase
from django.urls import resolve, reverse
# Local apps
from gym.views import LoginView


class LoginViewTests(TestCase):
    def setUp(self):
        view_name = reverse('gym:login')
        self.view_class = resolve(view_name).func.view_class

    def test_url_resolves_to_view(self):
        self.assertIs(self.view_class, LoginView)

    def test_view_inherits_from_auth_LoginView(self):
        auth = views.LoginView
        view = LoginView
        assert issubclass(view, auth), '{} {} {}'.format(
            view, 'is not a subclass of ', auth
        )

    def test_template_name_attribute_assigned_to_login_string(self):
        string = self.view_class.template_name
        expected_string = 'login.html'
        self.assertEqual(string, expected_string)

    def test_redirect_authenticated_user_attribute_assigned_to_True(self):
        self.assertTrue(self.view_class.redirect_authenticated_user)
