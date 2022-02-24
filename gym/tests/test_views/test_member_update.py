# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.test import TestCase
from django.urls import resolve, reverse
from django.views.generic.edit import UpdateView
from gym.forms import MemberForm
from gym.models import Member
# Local apps
from gym.views import MemberUpdateView


class MemberUpdateViewTests(TestCase):
    def setUp(self):
        # Specific pk is not important.
        self.view_name = reverse('gym:member_update', kwargs={'pk': 1})
        self.view_class = resolve(self.view_name).func.view_class

    def test_url_resolves_to_view(self):
        self.assertIs(
            self.view_class,
            MemberUpdateView
        )

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

    def test_login_url_attribute_assigned_to_login_namespace(self):
        namespace = self.view_class.login_url
        expected_namespace = reverse('gym:login')
        self.assertEqual(namespace, expected_namespace)

    def test_template_name_attribute_assigned_to_member_form_string(self):
        string = self.view_class.template_name
        expected_string = 'member_form.html'
        self.assertEqual(string, expected_string)

    def test_form_class_attribute_assigned_to_MemberForm_form(self):
        form = self.view_class.form_class
        expected_form = MemberForm
        self.assertEqual(form, expected_form)

    def test_model_attribute_assigned_to_Member_model(self):
        model = self.view_class.model
        expected_model = Member
        self.assertEqual(model, expected_model)

    def test_success_url_attribute_assigned_to_index_namespace(self):
        namespace = self.view_class.success_url
        expected_namespace = reverse('gym:index')
        self.assertEqual(namespace, expected_namespace)
