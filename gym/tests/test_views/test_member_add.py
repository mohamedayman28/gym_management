# Django
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import reverse
from django.test import RequestFactory, TestCase
from django.urls import resolve
# Local apps
from gym.views import HomePageView, LogInView, MemberAddView
# Third party
from mixer.backend.django import mixer


class MemberAddViewTests(TestCase):
    def setUp(self):
        self.user = mixer.blend('auth.User')
        self.view_name = reverse('member_add')
        self.request = RequestFactory().post(self.view_name)
        # Authenticate a user.
        self.request.user = self.user

    def test_url_resolves_to_the_correct_view(self):
        found = resolve(self.view_name)
        self.assertIs(found.func.view_class, MemberAddView)

    def test_PATCH_not_allowed(self):
        request = RequestFactory().patch(self.view_name)
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PATCH_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().patch(self.view_name)
        request.user = AnonymousUser()
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PATCH_not_allowed_from_authenticated_user(self):
        request = RequestFactory().patch(self.view_name)
        request.user = self.user
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed(self):
        request = RequestFactory().delete(self.view_name)
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().delete(self.view_name)
        request.user = AnonymousUser()
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed_from_authenticated_user(self):
        request = RequestFactory().delete(self.view_name)
        request.user = self.user
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed(self):
        request = RequestFactory().put(self.view_name)
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().put(self.view_name)
        request.user = AnonymousUser()
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed_from_authenticated_user(self):
        request = RequestFactory().put(self.view_name)
        request.user = self.user
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_GET_not_allowed(self):
        request = RequestFactory().get(self.view_name)
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_GET_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().get(self.view_name)
        request.user = AnonymousUser()
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_GET_not_allowed_from_authenticated_user(self):
        request = RequestFactory().get(self.view_name)
        request.user = self.user
        response = MemberAddView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_view_returns_HttpResponse(self):
        response = MemberAddView.as_view()(self.request)
        self.assertIsInstance(response, HttpResponse)

    def test_view_returns_HttpResponse_when_unauthenticated_user(self):
        self.request.user = AnonymousUser()
        response = MemberAddView.as_view()(self.request)
        self.assertIsInstance(response, HttpResponse)

    def test_view_redirects_unauthenticated_user(self):
        self.request.user = AnonymousUser()
        response = MemberAddView.as_view()(self.request)
        self.assertEqual(response.status_code, 302)

    def test_view_redirects_unauthenticated_user_to_correct_view(self):
        self.request.user = AnonymousUser()
        response = MemberAddView.as_view()(self.request)
        found = resolve(response.url)
        self.assertIs(found.func.view_class, LogInView)

    def test_valid_form_redirects_to_correct_view(self):
        data = {
            'member': self.user.id,
            'first_name': 'Mohamed',
            'last_name': 'Ahmed',
            'gender': 'fl',
            'enrolled_date': '2021-2-1',
            'end_date': '2021-11-26',
        }

        request = RequestFactory().post(self.view_name, data=data)
        request.user = self.user

        response = MemberAddView.as_view()(request)
        found = resolve(response.url)

        self.assertIs(found.func.view_class, HomePageView)

    def test_invalid_form_renders_correct_template(self):
        password = 'scrumptious'
        self.user.set_password(password)
        self.user.save()
        self.client.login(username=self.user.username, password=password)

        response = self.client.post(self.view_name, data={})
        self.assertTemplateUsed(response, 'member_form.html')
