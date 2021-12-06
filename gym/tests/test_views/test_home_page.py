# Python
import datetime
# Django
from django.contrib.auth.models import AnonymousUser
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import reverse
from django.test import RequestFactory, TestCase
from django.urls import resolve
# Local apps
from gym.models import Member
from gym.views import HomePageView
# Third party
from mixer.backend.django import mixer


class HomePageViewTests(TestCase):
    def setUp(self):
        self.view_name = reverse('home_page')
        self.user = mixer.blend('auth.User')

    def test_url_resolves_to_the_correct_view(self):
        found = resolve(self.view_name)
        self.assertIs(found.func.view_class, HomePageView)

    def test_POST_not_allowed(self):
        request = RequestFactory().post(self.view_name)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_POST_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = AnonymousUser()
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_POST_not_allowed_from_authenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = self.user
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PATCH_not_allowed(self):
        request = RequestFactory().patch(self.view_name)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PATCH_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().patch(self.view_name)
        request.user = AnonymousUser()
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PATCH_not_allowed_from_authenticated_user(self):
        request = RequestFactory().patch(self.view_name)
        request.user = self.user
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed(self):
        request = RequestFactory().delete(self.view_name)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = AnonymousUser()
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_DELETE_not_allowed_from_authenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = self.user
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed(self):
        request = RequestFactory().put(self.view_name)
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed_from_unauthenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = AnonymousUser()
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_PUT_not_allowed_from_authenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = self.user
        response = HomePageView.as_view()(request)
        self.assertEqual(response.status_code, 405)

    def test_view_returns_HttpResponse(self):
        request = RequestFactory().get(self.view_name)
        response = HomePageView.as_view()(request)
        self.assertIsInstance(response, HttpResponse)

    def test_view_returns_HttpResponse_when_unauthenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = AnonymousUser()
        response = HomePageView.as_view()(request)
        self.assertIsInstance(response, HttpResponse)

    def test_view_returns_HttpResponse_when_authenticated_user(self):
        request = RequestFactory().post(self.view_name)
        request.user = self.user
        response = HomePageView.as_view()(request)
        self.assertIsInstance(response, HttpResponse)

    def test_view_renders_correct_template(self):
        response = self.client.get(self.view_name)
        self.assertTemplateUsed(response, 'home_page.html')

    def test_view_renders_correct_template_when_authenticated_user(self):
        # Create user and login.
        user = mixer.blend('auth.User')
        password = 'scrumptious'
        self.user.set_password(password)
        self.user.save()
        self.client.login(username=user.username, password=password)

        response = self.client.get(self.view_name)
        self.assertTemplateUsed(response, 'home_page.html')

    def test_view_renders_correct_template_when_unauthenticated_user(self):
        # NOTE: User is logged-out by default.
        response = self.client.get(self.view_name)
        self.assertTemplateUsed(response, 'home_page.html')

    def test_view_context_has_members_key(self):
        response = self.client.get(self.view_name)
        self.assertIsNotNone(response.context.get('members'))

    def test_view_context_members_key_is_a_QuerySet(self):
        response = self.client.get(self.view_name)
        self.assertIsInstance(response.context.get('members'), QuerySet)

    def test_view_context_members_key_is_a_Member_queryset(self):
        mixer.cycle().blend(
            Member,
            # Call save() with its default behavior.
            is_cleaned=True,
            # Avoid raise from save() or clean() if enrolled_date >= end_date.
            end_date=datetime.datetime.now() + datetime.timedelta(days=1)
        )

        response = self.client.get(self.view_name)
        # Override Member.Meta.ordering to have different results.
        members_queryset = response.context.get('members').order_by(
            'first_name'
        )

        first_member_object = members_queryset.first()
        second_member_object = members_queryset.last()

        self.assertIsInstance(first_member_object, Member)
        self.assertIsInstance(second_member_object, Member)
