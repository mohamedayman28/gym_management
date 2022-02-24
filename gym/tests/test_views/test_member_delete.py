# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.test import TestCase
from django.urls import resolve, reverse
from django.views.generic.edit import DeleteView
# Local apps
from gym.models import Member
from gym.views import MemberDeleteView
# Third party
from mixer.backend.django import mixer


class MemberDeleteViewTests(TestCase):
    def setUp(self):
        self.view_name = reverse('gym:member_delete', kwargs={'pk': 1})
        self.view_class = resolve(self.view_name).func.view_class
        # Create User and login
        user = mixer.blend('auth.User')
        self.client.force_login(user)

    def test_url_resolves_to_view(self):
        self.assertIs(self.view_class, MemberDeleteView)

    def test_view_inherits_from_mixins_LoginRequiredMixin(self):
        mixins = LoginRequiredMixin
        view = MemberDeleteView
        assert issubclass(view, mixins), '{} {} {}'.format(
            view, 'is not a subclass of ', mixins
        )

    def test_view_inherits_from_generic_DeleteView(self):
        generic = DeleteView
        view = MemberDeleteView
        assert issubclass(view, generic), '{} {} {}'.format(
            view, 'is not a subclass of ', generic
        )

    def test_login_url_attribute_assigned_to_login_namespace(self):
        namespace = self.view_class.login_url
        expected_namespace = reverse('gym:login')
        self.assertEqual(namespace, expected_namespace)

    def test_template_name_attribute_assigned_to_member_confirm_delete_string(self):
        string = self.view_class.template_name
        expected_string = 'member_confirm_delete.html'
        self.assertEqual(string, expected_string)

    def test_model_attribute_assigned_to_Member_model(self):
        model = self.view_class.model
        expected_model = Member
        self.assertIs(model, expected_model)

    def test_template_name_field_attribute_assigned_to_member_string(self):
        string = self.view_class.template_name_field
        expected_string = 'member'
        self.assertEqual(string, expected_string)

    def test_success_url_attribute_assigned_to_index_namespace(self):
        namespace = self.view_class.success_url
        expected_namespace = reverse('gym:index')
        self.assertEqual(namespace, expected_namespace)
