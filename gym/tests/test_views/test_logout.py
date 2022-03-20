# Django
from django.contrib.auth import views
from django.test import TestCase
from django.urls import resolve, reverse
# Local apps
from gym.views import LogoutView


class LogoutViewUrlResolveTests(TestCase):
    def test_url_resolves_to_view(self):
        view_name = reverse('gym:logout')
        view_class = resolve(view_name).func.view_class

        self.assertIs(view_class, LogoutView)


class LogoutViewInheritanceTests(TestCase):
    def test_view_inherit_from_auth_LogoutView(self):
        auth = views.LogoutView
        view = LogoutView

        assert issubclass(view, auth), '{} {} {}'.format(
            view, 'is not a subclass of ', auth
        )


class LogoutViewAttributesTests(TestCase):
    def test_template_name_attribute_is_assigned_to_logged_out_string(self):
        view_name = reverse('gym:logout')
        view_class = resolve(view_name).func.view_class

        expected_string = 'logged_out.html'
        current_string = view_class.template_name

        self.assertEqual(expected_string, current_string)
