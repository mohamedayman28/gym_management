# Django
from django.test import TestCase
# Local apps
from gym import urls
from gym.api import urls as api_urls


class AppNameVariableTests(TestCase):
    def setUp(self):
        # If there is no attribute, AttributeError will raise.
        self.app_name = urls.app_name

    def test_app_name_value_is_string(self):
        self.assertIsInstance(self.app_name, str)

    def test_app_name_value_is_correct(self):
        expected_value = 'gym'
        current_app_name_value = self.app_name
        self.assertEqual(expected_value, current_app_name_value)


class UrlPatternsVariableTests(TestCase):
    def setUp(self):
        # If there is no attribute, AttributeError will raise.
        self.urls = urls.urlpatterns

    def test_urlpatterns_is_assigned_to_list(self):
        expected_datatype = list
        current_datatype = type(self.urls)
        self.assertIs(expected_datatype, current_datatype)

    def test_urlpatterns_length_is_correct(self):
        # 7 means 7 URL patterns.
        expected_length = 7
        current_length = len(self.urls)
        self.assertEqual(expected_length, current_length)

    def test_urlpatterns_value_has_correct_order(self):
        """
        NOTE: This is a personal reference function, you can skip it.

        Not needed, next test class will check each url index.
        """


class HomePageURLTests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[0]

    def test_path_pattern_is_correct(self):
        expected_pattern = ''
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_second_non_default_parameter_is_correct(self):
        """
        Second non default parameter is the callabale view.
        """
        expected_view = 'gym.views.HomePageView'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)

    def test_path_default_parameter_is_not_assigned_to_default_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        self.assertIsNotNone(self.url.name)

    def test_path_default_parameter_is_assigned_to_correct_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        expected_name = 'index'
        current_name = self.url.name
        self.assertEqual(expected_name, current_name)


class MemberFormURLTests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[1]

    def test_path_pattern_is_correct(self):
        expected_pattern = 'member/form/'
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_second_non_default_parameter_is_correct(self):
        """
        Second non default parameter is the callabale view.
        """
        expected_view = 'gym.views.MemberFormView'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)

    def test_path_default_parameter_is_not_assigned_to_default_value(self):
        """
        Default parameter is path(, ,name=)  and its default value is None
        """
        self.assertIsNotNone(self.url.name)

    def test_path_default_parameter_is_assigned_to_correct_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        expected_name = 'member_form'
        current_name = self.url.name
        self.assertEqual(expected_name, current_name)


class MemberDeleteURLTests(TestCase):
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
        expected_view = 'gym.views.MemberDeleteView'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)

    def test_path_default_parameter_is_not_assigned_to_default_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        self.assertIsNotNone(self.url.name)

    def test_path_default_parameter_is_assigned_to_correct_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        expected_name = 'member_delete'
        current_name = self.url.name
        self.assertEqual(expected_name, current_name)


class MemberUpdateURLTests(TestCase):
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
        expected_view = 'gym.views.MemberUpdateView'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)

    def test_path_default_parameter_is_not_assigned_to_default_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        self.assertIsNotNone(self.url.name)

    def test_path_default_parameter_is_assigned_to_correct_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        expected_name = 'member_update'
        current_name = self.url.name
        self.assertEqual(expected_name, current_name)


class LoginURLTests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[4]

    def test_path_pattern_is_correct(self):
        expected_pattern = 'login/'
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_second_non_default_parameter_is_correct(self):
        """
        Second non default parameter is the callabale view.
        """
        expected_view = 'gym.views.LoginView'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)

    def test_path_default_parameter_is_not_assigned_to_default_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        self.assertIsNotNone(self.url.name)

    def test_path_default_parameter_is_assigned_to_correct_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        expected_name = 'login'
        current_name = self.url.name
        self.assertEqual(expected_name, current_name)


class LogoutURLTests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[5]

    def test_path_pattern_is_correct(self):
        expected_pattern = 'logout/'
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_second_non_default_parameter_is_correct(self):
        """
        Second non default parameter is the callabale view.
        """
        expected_view = 'gym.views.LogoutView'
        current_view = self.url.lookup_str
        self.assertEqual(expected_view, current_view)

    def test_path_default_parameter_is_not_assigned_to_default_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        self.assertIsNotNone(self.url.name)

    def test_path_default_parameter_is_assigned_to_correct_value(self):
        """
        Default parameter is path(, ,name=) and its default value is None.
        """
        expected_name = 'logout'
        current_name = self.url.name
        self.assertEqual(expected_name, current_name)


class APIURLTests(TestCase):
    def setUp(self):
        self.url = urls.urlpatterns[6]

    def test_path_pattern_is_correct(self):
        expected_pattern = 'api/'
        current_pattern = str(self.url.pattern)
        self.assertEqual(expected_pattern, current_pattern)

    def test_path_uses_include_function(self):
        """
        urlconf_module attribute means include function is used, otherwise
        AttributeError will raise by default.
        """
        self.url.urlconf_module  # pylint: disable=pointless-statement

    def test_included_module_is_correct(self):
        self.assertIs(api_urls, self.url.urlconf_module)
