# Python
import datetime
# Django
from django.contrib.admin import site
from django.contrib.admin.sites import AdminSite
from django.test import TestCase
# Local apps
from gym.admin import MemberAdmin
from gym.models import Member
# Third party
from mixer.backend.django import mixer


class MemberAdminTests(TestCase):
    def setUp(self):
        admin_site = AdminSite()
        self.admin = MemberAdmin(Member, admin_site)
        # NOTE: Mixer sets models.field(default) if no value assigned.
        self.member = mixer.blend(
            'gym.Member',
            is_cleaned=True,  # Call save() default behavior.
            end_date=datetime.datetime.now() + datetime.timedelta(days=1)
        )

    def test_Member_model_is_registered(self):
        self.assertTrue(site.is_registered(Member))

    def test_Member_model_is_not_registered_by_itself(self):
        string = site._registry.get(Member).__str__()  # pylint: disable=protected-access
        # ModelAdmin class is the default admin representation.
        self.assertNotEqual(string, 'gym.ModelAdmin')

    def test_Member_model_is_registered_with_MemberAdmin(self):
        model = site._registry.get(Member)  # pylint: disable=protected-access
        self.assertIsInstance(model, MemberAdmin)

    def test_admin_has_remaining_days_method(self):
        """
        If no method, AttributeError will raise by default.
        """
        self.admin.remaining_days  # pylint: disable=pointless-statement

    def test_remaining_days_method_returns_integer(self):
        self.assertIsInstance(
            self.admin.remaining_days(self.member),
            int
        )

    def test_remaining_days_method_returns_positive_integer(self):
        self.assertGreater(
            self.admin.remaining_days(self.member),
            0
        )

    def test_list_display_attribute_assigned_to_a_tuple_datatype(self):
        self.assertIsInstance(
            self.admin.list_display,
            tuple
        )

    def test_list_display_attribute_has_correct_fields_order(self):
        fields = self.admin.list_display
        expected_fields = ('__str__', 'remaining_days')
        self.assertEqual(fields, expected_fields)
