# Django
from django.test import TestCase
# Local apps
from gym.forms import MemberForm
from gym.models import Member
# Third party
from mixer.backend.django import mixer


class MemberSerializerAttributeTests(TestCase):
    def test_serializer_has_member_id_attribute(self):
        self.fail('Stopped here!!')

    def test_member_id_attribute_is_assigned_to_IntegerField(self):
        self.fail('Stopped here!!')

    def test_IntegerField_default_argument_is_not_assigned_to_default_value(self):
        """
        Default argument is IntegerField(source= ) and its default value is
        """
        self.fail('Stopped here!!')

    def test_IntegerField_default_argument_is_assigned_to_correct_value(self):
        self.fail('Stopped here!!')


class MemberSerializerMetaAttributesTests(TestCase):
    def setUp(self):
        self.meta_class = MemberForm.Meta

    def test_Meta_model_attribute_is_not_assigned_to_default_value(self):
        """
        Default value is
        """
        self.fail('Stopped here!!')

    def test_Meta_model_attribute_is_assigned_to_Member_model(self):
        self.assertIs(
            self.meta_class.model,
            Member
        )

    def test_Meta_fields_attribute_is_not_assigned_to_default_value(self):
        """
        Default value is
        """
        self.fail('Stopped here!!')

    def test_Meta_fields_attribute_is_not_assigned_to__all__string(self):
        # NOTE: Using "__all__" is not recommended by Django.
        self.assertNotIsInstance(
            self.meta_class.fields,
            str
        )

    def test_Meta_fields_attribute_is_assigned_to_a_list_datatype(self):
        self.assertIsInstance(
            self.meta_class.fields,
            list
        )

    def test_Meta_fields_attribute_has_correct_fields_order(self):
        current_fields = self.meta_class.fields
        #  sort() Unordered list will test both, order of fields and
        # that fields are as expected.
        expected_fields = ['end_date', 'gender', 'last_name', 'enrolled_date',
                           'first_name', 'user']
        current_fields.sort()
        expected_fields.sort()
        self.assertEqual(expected_fields, current_fields)


class MemberSerializerFieldsTests(TestCase):
    def setUp(self):
        self.user = mixer.blend('auth.User')

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

    def test_end_date_field_raises_correct_validation_error(self):
        form = MemberForm({
            'member': self.user,
            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
            'enrolled_date': '2021-11-26',
            'end_date': '2009-2-1'  # Error.
        })
        current_error = form.errors.get('end_date')  # Returns list object.
        expected_error = 'The date must be in the future by at least one day.'
        self.assertEqual(expected_error, current_error[0])
