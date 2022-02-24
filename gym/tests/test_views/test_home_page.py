# Django
from django.shortcuts import reverse
from django.test import TestCase
from django.urls import resolve
from django.views.generic.list import ListView
# Local apps
from gym.views import HomePageView
from gym.models import Member
# Third party
from mixer.backend.django import mixer


class HomePageViewTests(TestCase):
    def setUp(self):
        self.view_name = reverse('gym:index')
        self.view_class = resolve(self.view_name).func.view_class

    def test_url_resolves_to_view(self):
        self.assertIs(self.view_class, HomePageView)

    def test_view_inherits_from_generic_ListView(self):
        generic = ListView
        view = HomePageView
        assert issubclass(view, generic), '{} {} {}'.format(
            view, 'is not a subclass of ', generic
        )

    def test_template_name_attribute_assigned_to_index_string(self):
        string = self.view_class.template_name
        expected_string = 'index.html'
        self.assertEqual(string, expected_string)

    def test_model_attribute_assigned_to_Member_model(self):
        model = self.view_class.model
        expected_model = Member
        self.assertIs(model, expected_model)

    def test_context_object_name_attribute_assigned_to_members_string(self):
        string = self.view_class.context_object_name
        expected_string = 'members'
        self.assertEqual(string, expected_string)
