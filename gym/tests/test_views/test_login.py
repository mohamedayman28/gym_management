# Django
from django.contrib.auth import views
from django.test import TestCase
from django.urls import resolve, reverse
# Local apps
from gym.views import LoginView


class LoginViewUrlResolveTest(TestCase):
    def test_url_resolves_to_view(self):
        view_name = reverse('gym:login')
        view_class = resolve(view_name).func.view_class

        self.assertIs(view_class, LoginView)


class LoginViewInheritanceTest(TestCase):
    def test_view_inherits_from_auth_LoginView(self):
        auth = views.LoginView
        view = LoginView

        assert issubclass(view, auth), '{} {} {}'.format(
            view, 'is not a subclass of ', auth
        )


class LoginViewAttributesTests(TestCase):
    def setUp(self):
        view_name = reverse('gym:login')
        self.view_class = resolve(view_name).func.view_class

    def test_template_name_attribute_is_assigned_to_login_string(self):
        expected_string = 'login.html'
        current_string = self.view_class.template_name

        self.assertEqual(expected_string, current_string)

    def test_redirect_authenticated_user_attribute_is_assigned_to_True(self):
        self.assertTrue(self.view_class.redirect_authenticated_user)
