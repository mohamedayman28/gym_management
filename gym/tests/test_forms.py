# Django
from django.test import TestCase
# Local apps
from gym.forms import MemberForm
from gym.models import Member
# Third party
from mixer.backend.django import mixer


class MemberFormTests(TestCase):
    def setUp(self):
        self.meta_class = MemberForm.Meta
        self.user = mixer.blend('auth.User')

    def test_Meta_model_attribute_assigned_to_Member_model(self):
        self.assertIs(
            self.meta_class.model,
            Member
        )

    def test_Meta_fields_attribute_not_assigned_to__all__string(self):
        # NOTE: Using "__all__" is not recommended by Django.
        self.assertNotIsInstance(
            self.meta_class.fields,
            str
        )

    def test_Meta_fields_attribute_assigned_to_a_list_datatype(self):
        self.assertIsInstance(
            self.meta_class.fields,
            list
        )

    def test_Meta_fields_attribute_has_expected_fields_order(self):
        fields = self.meta_class.fields
        #  sort() Unordered list will test both, order of fields and
        # that fields are as expected.
        expected_fields = ['end_date', 'gender', 'last_name', 'enrolled_date',
                           'first_name', 'user']
        fields.sort()
        expected_fields.sort()
        self.assertEqual(fields, expected_fields)

    def test_end_date_field_raises(self):
        form = MemberForm({
            'member': self.user,
            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
            'enrolled_date': '2021-11-26',
            'end_date': '2009-2-1'  # Error.
        })
        self.assertIn('end_date', form.errors)

    def test_end_date_field_raises_expected_validation_error(self):
        form = MemberForm({
            'member': self.user,
            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
            'enrolled_date': '2021-11-26',
            'end_date': '2009-2-1'  # Error.
        })
        error = form.errors.get('end_date')  # Returns list object.
        expected_error = 'The date must be in the future by at least one day.'
        self.assertEqual(error[0], expected_error)
