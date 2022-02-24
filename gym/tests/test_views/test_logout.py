# Django
from django.contrib.auth import views
from django.test import TestCase
from django.urls import resolve, reverse
# Local apps
from gym.views import LogoutView


class LogoutViewTests(TestCase):
    def setUp(self):
        self.view_name = reverse('gym:logout')
        self.view_class = resolve(self.view_name).func.view_class

    def test_url_resolves_to_view(self):
        self.assertIs(self.view_class, LogoutView)

    def test_view_inherit_from_auth_LogoutView(self):
        auth = views.LogoutView
        view = LogoutView
        assert issubclass(view, auth), '{} {} {}'.format(
            view, 'is not a subclass of ', auth
        )

    def test_template_name_attribute_assigned_to_logged_out_string(self):
        string = self.view_class.template_name
        expected_string = 'logged_out.html'
        self.assertEqual(string, expected_string)
