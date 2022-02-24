# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.test import TestCase
from django.urls import resolve, reverse
from django.views.generic.edit import CreateView
# Local apps
from gym.forms import MemberForm
from gym.views import MemberFormView
# Third party
from mixer.backend.django import mixer


class MemberFormViewTests(TestCase):
    def setUp(self):
        self.view_name = reverse('gym:member_form')
        self.view_class = resolve(self.view_name).func.view_class
        # Create User and login.
        self.user = mixer.blend('auth.User')
        self.client.force_login(self.user)

    def test_url_resolves_to_view(self):
        self.assertIs(self.view_class, MemberFormView)

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
        self.assertIs(form, expected_form)

    def test_success_url_attribute_assigned_to_index_namespace(self):
        namespace = self.view_class.success_url
        expected_namespace = reverse('gym:index')
        self.assertEqual(namespace, expected_namespace)
