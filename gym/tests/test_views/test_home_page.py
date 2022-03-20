# Django
from django.shortcuts import reverse
from django.test import TestCase
from django.urls import resolve
from django.views.generic.list import ListView
# Local apps
from gym.views import HomePageView
from gym.models import Member


class HomePageViewUrlResolveTest(TestCase):
    def test_url_resolves_to_view(self):
        view_name = reverse('gym:index')
        view_class = resolve(view_name).func.view_class

        self.assertIs(view_class, HomePageView)


class HomePageViewInheritanceTest(TestCase):
    def test_view_inherits_from_generic_ListView(self):
        generic = ListView
        view = HomePageView

        assert issubclass(view, generic), '{} {} {}'.format(
            view, 'is not a subclass of ', generic
        )


class HomePageViewAttributesTests(TestCase):
    def setUp(self):
        view_name = reverse('gym:index')
        self.view_class = resolve(view_name).func.view_class

    def test_template_name_attribute_is_assigned_to_index_string(self):
        expected_string = 'index.html'
        current_string = self.view_class.template_name

        self.assertEqual(expected_string, current_string)

    def test_model_attribute_is_assigned_to_Member_model(self):
        expected_model = Member
        current_model = self.view_class.model

        self.assertIs(expected_model, current_model)

    def test_context_object_name_attribute_is_assigned_to_members_string(self):
        expected_string = 'members'
        current_string = self.view_class.context_object_name

        self.assertEqual(expected_string, current_string)
