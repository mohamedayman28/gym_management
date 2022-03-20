# Django
from django.test import TestCase
# Local apps
from gym.api import urls


class ApiPatternsVariableTests(TestCase):
    def setUp(self):
        # If there is no attribute, AttributeError will raise.
        self.urls = urls.urlpatterns

    def test_urlpatterns_is_assigned_to_list(self):
        expected_datatype = list
        current_datatype = type(self.urls)
        self.assertIs(expected_datatype, current_datatype)

    def test_urlpatterns_length_is_correct(self):
        # 4 means 4 URL patterns.
        expected_length = 4
        current_length = len(self.urls)
        self.assertEqual(expected_length, current_length)

    def test_urlpatterns_value_has_correct_order(self):
        """
        NOTE: This is a personal reference function, you can skip it.

        Not needed, next test class will check each url index.
        """


class ApiMemberListAPIURLTests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[0]

    def test_path_pattern_is_correct(self):
        expected_pattern = 'member/list/'
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_second_non_default_parameter_is_correct(self):
        """
        Second non default parameter is the callabale view.
        """
        expected_view = 'gym.api.views.MemberListAPI'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)


class ApiMemberCreateAPITests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[1]

    def test_path_pattern_is_correct(self):
        expected_pattern = 'member/create/'
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_second_non_default_parameter_is_correct(self):
        """
        Second non default parameter is the callabale view.
        """
        expected_view = 'gym.api.views.MemberCreateAPI'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)


class ApiMemberDeleteAPITests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[2]

    def test_path_pattern_is_correct(self):
        expected_pattern = 'member/<int:pk>/delete/'
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_converter_accepts_integer_value_only(self):
        """
        Correct pattern should contain an integer variable, otherwise None will
        return.
        """
        expected_pattern = 'member/qwe/delete/'
        self.assertIsNone(self.url.resolve(expected_pattern))

    def test_path_second_non_default_parameter_is_correct(self):
        """
        Second non default parameter is the callabale view.
        """
        expected_view = 'gym.api.views.MemberDeleteAPI'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)


class ApiMemberUpdateAPITests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[3]

    def test_path_pattern_is_correct(self):
        expected_pattern = 'member/<int:pk>/update/'
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_converter_accepts_integer_value_only(self):
        """
        Correct pattern should contain an integer variable, otherwise None will
        return.
        """
        expected_pattern = 'member/qwe/update/'
        self.assertIsNone(self.url.resolve(expected_pattern))

    def test_path_second_non_default_parameter_is_correct(self):
        """
        Second non default parameter is the callabale view.
        """
        expected_view = 'gym.api.views.MemberUpdateAPI'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)
