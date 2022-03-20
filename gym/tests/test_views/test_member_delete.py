# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.test import TestCase
from django.urls import resolve, reverse
from django.views.generic.edit import DeleteView
# Local apps
from gym.models import Member
from gym.views import MemberDeleteView


class MemberDeleteViewUrlResolveTests(TestCase):
    def test_url_resolves_to_view(self):
        # Specific pk is not important.
        view_name = reverse('gym:member_delete', kwargs={'pk': 1})
        view_class = resolve(view_name).func.view_class

        self.assertIs(view_class, MemberDeleteView)


class MemberDeleteViewInheritanceTests(TestCase):
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


class MemberDeleteViewAttributesTests(TestCase):
    def setUp(self):
        view_name = reverse('gym:member_delete', kwargs={'pk': 1})
        self.view_class = resolve(view_name).func.view_class

    def test_login_url_attribute_is_assigned_to_login_namespace(self):
        expected_namespace = reverse('gym:login')
        current_namespace = self.view_class.login_url

        self.assertEqual(expected_namespace, current_namespace)

    def test_model_attribute_is_assigned_to_Member_model(self):
        expected_model = Member
        current_model = self.view_class.model

        self.assertIs(expected_model, current_model)

    def test_template_name_field_attribute_is_assigned_to_member_string(self):
        expected_string = 'member'
        current_string = self.view_class.template_name_field

        self.assertEqual(expected_string, current_string)

    def test_success_url_attribute_is_assigned_to_index_namespace(self):
        expected_namespace = reverse('gym:index')
        current_namespace = self.view_class.success_url

        self.assertEqual(expected_namespace, current_namespace)
