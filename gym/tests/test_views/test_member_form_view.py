# Django
from django.contrib.auth.models import AnonymousUser
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import reverse
from django.test import RequestFactory, TestCase
from django.urls import resolve
# Local apps
from gym.forms import MemberForm
from gym.views import MemberFormView
# Third party
from mixer.backend.django import mixer


class MemberFormViewTests(TestCase):
    def setUp(self):
        self.view_name = reverse('member_form')
        self.user = mixer.blend('auth.User')

    def test_url_resolves_to_the_correct_view(self):
        found = resolve(self.view_name)
        self.assertIs(found.func.view_class, MemberFormView)

    def test_POST_not_allowed(self):
        request = RequestFactory().post(self.view_name)
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_POST_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = AnonymousUser()
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_POST_not_allowed_from_authenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = self.user
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PATCH_not_allowed(self):
        request = RequestFactory().patch(self.view_name)
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PATCH_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().patch(self.view_name)
        request.user = AnonymousUser()
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PATCH_not_allowed_from_authenticated_user(self):
        request = RequestFactory().patch(self.view_name)
        request.user = self.user
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed(self):
        request = RequestFactory().delete(self.view_name)
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().delete(self.view_name)
        request.user = AnonymousUser()
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed_from_authenticated_user(self):
        request = RequestFactory().delete(self.view_name)
        request.user = self.user
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed(self):
        request = RequestFactory().put(self.view_name)
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().put(self.view_name)
        request.user = AnonymousUser()
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed_from_authenticated_user(self):
        request = RequestFactory().put(self.view_name)
        request.user = self.user
        response = MemberFormView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_view_returns_HttpResponse(self):
        request = RequestFactory().get(self.view_name)
        response = MemberFormView.as_view()(request)
        self.assertIsInstance(response, HttpResponse)

    def test_view_returns_HttpResponse_when_unauthenticated_user(self):
        request = RequestFactory().get(self.view_name)
        request.user = AnonymousUser()
        response = MemberFormView.as_view()(request)
        self.assertIsInstance(response, HttpResponse)

    def test_view_returns_HttpResponse_when_authenticated_user(self):
        request = RequestFactory().get(self.view_name)
        request.user = self.user
        response = MemberFormView.as_view()(request)
        self.assertIsInstance(response, HttpResponse)

    def test_view_renders_correct_template(self):
        response = self.client.get(self.view_name)
        self.assertTemplateUsed(response, 'member_form.html')

    # NOTE: By default client.logout()

    def test_view_renders_correct_template_when_authenticated_user(self):
        # Create user and login.
        user = mixer.blend('auth.User')
        password = 'scrumptious'
        self.user.set_password(password)
        self.user.save()
        self.client.login(username=user.username, password=password)

        response = self.client.get(self.view_name)
        self.assertTemplateUsed(response, 'member_form.html')

    def test_view_renders_correct_template_when_unauthenticated_user(self):
        # NOTE: User is logged-out by default.
        response = self.client.get(self.view_name)
        self.assertTemplateUsed(response, 'member_form.html')

    def test_view_context_has_form_key(self):
        response = self.client.get(self.view_name)
        form = response.context.get('form')
        self.assertIsNotNone(form)

    def test_view_context_form_key_is_ModelForm_instance(self):
        response = self.client.get(self.view_name)
        form = response.context.get('form')
        self.assertIsInstance(form, ModelForm)

    def test_view_context_form_key_is_correct_form(self):
        response = self.client.get(self.view_name)
        form = response.context.get('form')
        self.assertIsInstance(form, MemberForm)
