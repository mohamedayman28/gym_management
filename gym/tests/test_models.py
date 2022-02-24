# Python
import datetime
# Django
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth.models import User
# Local apps
from gym.models import Member
# Third party
from mixer.backend.django import Mixer

#   fake: Randomize generated values, for every initialization
# - e.g. apple, !@#W@#!, ... etc - that allows covering unexpected test cases.
mixer = Mixer(fake=False)


class MemberTests(TestCase):
    def setUp(self):
        # NOTE: Mixer sets models.field(default) if no value assigned.
        self.member = mixer.blend(
            'gym.Member',
            is_cleaned=True,  # Call save() default behavior.
            end_date=datetime.datetime.now() + datetime.timedelta(days=1)
        )
        self.member_meta = self.member._meta  # pylint: disable=protected-access

    def test_save_method_triggers_clean_method(self):
        """
        member.end_date must be in the future from member.enrolled_date by at
        least 2 days.

        save() does not make fields validation, so if ValidationError occur
        that's mean that clean() is called.
        """
        self.member.end_date = datetime.datetime.now()
        self.member.is_cleaned = False
        with self.assertRaises(ValidationError):
            self.member.save()

    def test_model_has_user_attribute(self):
        """
        If no attribute, FieldDoesNotExist will raise by default.
        """
        self.member_meta.get_field('user')

    def test_user_attribute_has_a_relation(self):
        self.assertTrue(self.member_meta.get_field('user').is_relation)

    def test_user_attribute_has_OneToOne_relation(self):
        self.assertTrue(
            self.member_meta.get_field('user').one_to_one
        )

    def test_user_attribute_related_to_User_model(self):
        self.assertIs(
            self.member_meta.get_field('user').related_model,
            User
        )

    def test_user_attribute_CASCADE_when_related_User_deleted(self):
        user = User.objects.create(username='Test', password='123123')
        self.member.member = user
        self.member.save()
        # With deleting the user related member should be deleted as well.
        user.delete()
        with self.assertRaises(Member.DoesNotExist):
            Member.objects.get(user=user)

    def test_model_has_first_name_attribute(self):
        """
        If no attribute, FieldDoesNotExist will raise by default.
        """
        self.member_meta.get_field('first_name')

    def test_first_name_attribute_has_10_as_max_length(self):
        self.assertEqual(
            self.member_meta.get_field('first_name').max_length,
            10
        )

    def test_model_has_gender_attribute(self):
        """
        If no attribute, FieldDoesNotExist will raise by default.
        """
        self.member_meta.get_field('gender')

    def test_gender_attribute_has_2_as_max_length(self):
        self.assertEqual(
            self.member_meta.get_field('gender').max_length,
            2
        )

    def test_gender_attribute_has_ml_and_fl_as_choices(self):
        self.assertEqual(
            self.member_meta.get_field('gender').choices,
            [('ml', 'Male'), ('fl', 'Female')]
        )

    def test_gender_attribute_accepts_value_from_assigned_choices_only(self):
        self.member.gender = 'off_list_choice'
        with self.assertRaises(ValidationError):
            self.member.full_clean()

    def test_gender_attribute_has_ml_as_default_value(self):
        self.assertEqual(
            self.member_meta.get_field('gender').default,
            'ml'
        )

    def test_model_has_enrolled_date_attribute(self):
        """
        If no attribute, FieldDoesNotExist will raise by default.
        """
        self.member_meta.get_field('enrolled_date')

    def test_enrolled_date_attribute_has_today_default_value(self):
        self.assertEqual(
            self.member_meta.get_field('enrolled_date').default,
            datetime.date.today
        )

    def test_model_has_end_date_attribute(self):
        """
        If no attribute, FieldDoesNotExist will raise by default.
        """
        self.member_meta.get_field('end_date')

    def test_end_date_attribute_has_today_default_value(self):
        self.assertEqual(
            self.member_meta.get_field('enrolled_date').default,
            datetime.date.today
        )

    def test_end_date_attribute_raises(self):
        """
        member.end_date must be in the future from member.enrolled_date by at
        least 2 days, otherwise it will raise.

        NOTE: self.member will not raise by default.
        """
        self.member.end_date = datetime.datetime.now()
        with self.assertRaises(ValidationError):
            self.member.full_clean()

    def test_str_method_returns_expected_value(self):
        self.assertEqual(
            self.member.__str__(),
            f'{self.member.first_name} {self.member.last_name}'
        )

    def test_model_has_get_remaining_days_method(self):
        """
        If no method, AttributeError will raise by default.
        """
        self.member.get_remaining_days  # pylint: disable=pointless-statement

    def test_get_remaining_days_method_returns_int(self):
        self.assertIsInstance(
            self.member.get_remaining_days(),
            int
        )

    def test_get_remaining_days_method_returns_positive_integer(self):
        self.assertGreater(
            self.member.get_remaining_days(),
            0
        )

    def test_model_has_get_gender_name_method(self):
        """
        If no method, AttributeError will raise by default.
        """
        self.member.get_gender_name  # pylint: disable=pointless-statement

    def test_get_gender_name_method_returns_str(self):
        self.assertIsInstance(
            self.member.get_gender_name(),
            str
        )

    def test_get_gender_name_method_returns_Female_when_assigned_to_fl(self):
        self.member.gender = 'fl'
        self.assertEqual(
            self.member.get_gender_name(),
            'Female'
        )

    def test_get_gender_name_method_returns_Male_when_assigned_to_ml(self):
        self.member.gender = 'ml'
        self.assertEqual(
            self.member.get_gender_name(),
            'Male'
        )

    def test_get_gender_name_method_returns_Unknown(self):
        """
        Returns Unknown when neither assigned to "fl" nor "ml".
        """
        self.member.gender = 'asdf'
        self.assertEqual(
            self.member.get_gender_name(),
            'Unknown'
        )
