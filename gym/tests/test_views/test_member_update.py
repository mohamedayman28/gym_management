# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.test import TestCase
from django.urls import resolve, reverse
from django.views.generic.edit import UpdateView
from gym.forms import MemberForm
from gym.models import Member
# Local apps
from gym.views import MemberUpdateView


class MemberUpdateViewUrlResolveTests(TestCase):
    def test_url_resolves_to_view(self):
        # Specific pk is not important.
        view_name = reverse('gym:member_update', kwargs={'pk': 1})
        view_class = resolve(view_name).func.view_class

        self.assertIs(
            view_class,
            MemberUpdateView
        )


class MemberUpdateViewInheritanceTests(TestCase):
    def test_view_inherits_from_mixins_LoginRequiredMixin(self):
        mixins = LoginRequiredMixin
        view = MemberUpdateView

        assert issubclass(view, mixins), '{} {} {}'.format(
            view, 'is not a subclass of ', mixins
        )

    def test_view_inherits_from_generic_UpdateView(self):
        generic = UpdateView
        view = MemberUpdateView

        assert issubclass(view, generic), '{} {} {}'.format(
            view, 'is not a subclass of ', generic
        )


class MemberUpdateViewAttributesTests(TestCase):
    def setUp(self):
        # Specific pk is not important.
        view_name = reverse('gym:member_update', kwargs={'pk': 1})
        self.view_class = resolve(view_name).func.view_class

    def test_login_url_attribute_is_assigned_to_login_namespace(self):
        expected_namespace = reverse('gym:login')
        current_namespace = self.view_class.login_url

        self.assertEqual(expected_namespace, current_namespace)

    def test_template_name_attribute_is_assigned_to_member_form_string(self):
        expected_string = 'member_form.html'
        current_string = self.view_class.template_name

        self.assertEqual(expected_string, current_string)

    def test_form_class_attribute_is_assigned_to_MemberForm_form(self):
        current_form = self.view_class.form_class
        expected_form = MemberForm

        self.assertEqual(expected_form, current_form)

    def test_model_attribute_is_assigned_to_Member_model(self):
        current_model = self.view_class.model
        expected_model = Member

        self.assertEqual(expected_model, current_model)

    def test_success_url_attribute_is_assigned_to_index_namespace(self):
        current_namespace = self.view_class.success_url
        expected_namespace = reverse('gym:index')

        self.assertEqual(expected_namespace, current_namespace)
