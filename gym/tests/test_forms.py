# Django
from django.test import TestCase
from django.contrib.auth.models import User
# Local apps
from gym.forms import MemberForm
from gym.models import Member
# Third party
from mixer.backend.django import mixer


class MemberFormTests(TestCase):
    def test_model_used_is_correct(self):
        model = MemberForm.Meta.model
        self.assertEqual(model, Member)
        self.assertIs(model, Member)

    def test_fields_not_called_using__all__(self):
        # NOTE: Calling fields using "__all__" is not recommended by Django.
        form_fields = MemberForm.Meta.fields
        self.assertNotIsInstance(form_fields, str)
        self.assertNotIsInstance(form_fields, dict)

    def test_fields_called_using_correct_datatype(self):
        form_fields = MemberForm.Meta.fields
        self.assertIsInstance(form_fields, list)

    def test_fields_specified_are_correct(self):
        form_fields = MemberForm.Meta.fields
        expected_fields = ['end_date', 'gender', 'last_name', 'enrolled_date',
                           'first_name', 'member']

        # Equal lists must have the same items order.
        form_fields.sort()
        expected_fields.sort()

        self.assertEqual(form_fields, expected_fields)

    def test_fields_order_is_correct(self):
        form_fields = MemberForm.Meta.fields
        expected_fields = ['member', 'first_name', 'last_name', 'gender',
                           'enrolled_date', 'end_date']
        self.assertEqual(form_fields, expected_fields)

    def test_member_field_is_required(self):
        form = MemberForm({
            'member': '',

            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
            'enrolled_date': '2021-2-1',
            'end_date': '2021-11-26',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('member', form.errors)

    def test_member_field_accepts_User_instance(self):
        user = mixer.blend('auth.User')
        form = MemberForm({
            'member': user,

            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
            'enrolled_date': '2021-2-1',
            'end_date': '2021-11-26',
        })

        self.assertTrue(form.is_valid())
        self.assertIsInstance(user, User)
        self.assertEqual(len(form.errors), 0)

    def test_first_name_field_is_required(self):
        form = MemberForm({
            'first_name': '',

            'last_name': 'Ahmed',
            'gender': 'fl',
            'enrolled_date': '2021-2-1',
            'end_date': '2021-11-26',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)

    def test_last_name_field_is_required(self):
        form = MemberForm({
            'last_name': '',

            'first_name': 'Sara',
            'gender': 'fl',
            'enrolled_date': '2021-2-1',
            'end_date': '2021-11-26',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('last_name', form.errors)

    def test_gender_field_is_required(self):
        form = MemberForm({
            'gender': '',

            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'enrolled_date': '2021-2-1',
            'end_date': '2021-11-26',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('gender', form.errors)

    def test_enrolled_date_field_is_required(self):
        form = MemberForm({
            'enrolled_date': '',

            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
            'end_date': '2021-11-26',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('enrolled_date', form.errors)

    def test_end_date_field_is_required(self):
        form = MemberForm({
            'end_date': '',

            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
            'enrolled_date': '2021-2-1',
        })

        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors)

    def test_end_date_field_raises(self):
        form = MemberForm({
            # enrolled_date should not be greater than end_date
            'enrolled_date': '2021-11-26',
            'end_date': '2009-2-1',

            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
        })

        self.assertIn('end_date', form.errors)

    def test_end_date_field_custom_validation_error_is_correct(self):
        form = MemberForm({
            'enrolled_date': '2021-11-26',
            'end_date': '2021-2-1',

            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
        })

        # Returns list object.
        error_message = form.errors.get('end_date')
        expected_message = 'The date must be in the future by at least one day.'

        self.assertEqual(error_message[0], expected_message)

    def test_form_update_database_when_valid_data(self):
        self.assertFalse(
            Member.objects.exists(),
            msg='Database (gym_member table) is empty before form.save()'
        )

        form = MemberForm({
            'member': mixer.blend('auth.User'),
            'enrolled_date': '2021-2-1',
            'end_date': '2021-11-26',
            'first_name': 'Sara',
            'last_name': 'Ahmed',
            'gender': 'fl',
        })
        if form.is_valid():
            form.save()

        self.assertTrue(
            Member.objects.exists(),
            msg='Database (gym_member table) is not empty after form.save()'
        )

    def test_form_do_not_update_database_when_invalid_data(self):
        self.assertFalse(
            Member.objects.exists(),
            msg='Database (gym_member table) is empty before form.save()'
        )

        form = MemberForm({})
        if form.is_valid():
            form.save()

        self.assertFalse(
            Member.objects.exists(),
            msg='Database (gym_member table) is empty after form.save()'
        )
