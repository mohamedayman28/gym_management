# Python
import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
# Third party
from mixer.backend.django import Mixer

#   fake: Randomize generated values, for every initialization
# - e.g. apple, !@#W@#!, ... etc - that allows covering unexpected test cases.
mixer = Mixer(fake=False)


class MemberTests(TestCase):
    def setUp(self):
        self.member = mixer.blend(
            'gym.Member',
            # Call save() with its default behavior.
            is_cleaned=True,
            # Avoid raise from save() or clean() if enrolled_date >= end_date.
            #   NOTE: Default value e.g. enrolled_date(default), will always be
            # assigned.
            end_date=datetime.datetime.now() + datetime.timedelta(days=1)
        )

    def test_first_name_attribute_is_required(self):
        self.member.first_name = ''
        with self.assertRaises(ValidationError):
            self.member.full_clean()

    def test_last_name_attribute_is_required(self):
        self.member.last_name = ''
        with self.assertRaises(ValidationError):
            self.member.full_clean()

    def test_gender_attribute_is_required(self):
        self.member.gender = ''
        with self.assertRaises(ValidationError):
            self.member.full_clean()

    def test_gender_attribute_accepts_data_from_choices_list_only(self):
        self.member.gender = 'asd'
        with self.assertRaises(ValidationError):
            self.member.full_clean()

    def test_end_date_attribute_always_greater_than_enrolled_date_attribute(self):
        self.member.end_date = datetime.datetime.now()
        with self.assertRaises(ValidationError):
            self.member.full_clean()

    def test_str_method_return_correct_value(self):
        str_return = f'{self.member.first_name} {self.member.last_name}'
        self.assertEqual(self.member.__str__(), str_return)

    def test_get_remaining_days_method_return_number_object(self):
        days = self.member.get_remaining_days()
        self.assertIsInstance(days, int)

    def test_get_remaining_days_method_return_positive_number(self):
        """
        Days difference should always be in the future(positive number).
        """
        days = self.member.get_remaining_days()
        self.assertNotEqual(days, 0)
        self.assertGreater(days, 0)

    def test_get_gender_method_return_string_object(self):
        gender = self.member.get_gender()
        self.assertIsInstance(gender, str)

    def test_get_gender_method_return_correct_gender_name(self):
        self.member.gender = 'fl'
        gender = self.member.get_gender()
        self.assertEqual(gender, 'Female')

        self.member.gender = 'ml'
        gender = self.member.get_gender()
        self.assertEqual(gender, 'Male')

        self.member.gender = 'asdf'
        gender = self.member.get_gender()
        self.assertEqual(gender, 'Unknown')
