# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.test import TestCase
from django.urls import resolve, reverse
from django.views.generic.edit import CreateView
# Local apps
from gym.forms import MemberForm
from gym.views import MemberFormView


class MemberFormViewUrlResolveTests(TestCase):
    def test_url_resolves_to_view(self):
        view_name = reverse('gym:member_form')
        view_class = resolve(view_name).func.view_class

        self.assertIs(view_class, MemberFormView)


class MemberFormViewInheritanceTests(TestCase):
    def test_view_inherits_from_mixins_LoginRequiredMixin(self):
        mixins = LoginRequiredMixin
        view = MemberFormView
        assert issubclass(view, mixins), '{} {} {}'.format(
            view, 'is not a subclass of ', mixins
        )

    def test_view_inherits_from_generic_FormView(self):
        generic = CreateView
        view = MemberFormView
        assert issubclass(view, generic), '{} {} {}'.format(
            view, 'is not a subclass of ', generic
        )


class MemberFormViewAttributesTests(TestCase):
    def setUp(self):
        view_name = reverse('gym:member_form')
        self.view_class = resolve(view_name).func.view_class

    def test_login_url_attribute_is_assigned_to_login_namespace(self):
        expected_namespace = reverse('gym:login')
        current_namespace = self.view_class.login_url

        self.assertEqual(expected_namespace, current_namespace)

    def test_template_name_attribute_is_assigned_to_member_form_string(self):
        current_string = self.view_class.template_name
        expected_string = 'member_form.html'

        self.assertEqual(expected_string, current_string)

    def test_form_class_attribute_is_assigned_to_MemberForm_form(self):
        current_form = self.view_class.form_class
        expected_form = MemberForm

        self.assertIs(expected_form, current_form)

    def test_success_url_attribute_is_assigned_to_index_namespace(self):
        current_namespace = self.view_class.success_url
        expected_namespace = reverse('gym:index')

        self.assertEqual(expected_namespace, current_namespace)
