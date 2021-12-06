# Python
import datetime

from django.contrib.auth.models import User
# Django
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Member(models.Model):
    # See overridden clean().
    is_cleaned = False
    # Choices constant
    MALE = 'ml'
    FEMALE = 'fl'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]
    # Relations
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    # Attributes
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    gender = models.CharField(max_length=2, choices=GENDERS, default=MALE)
    enrolled_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(default=datetime.date.today)

    class Meta:
        ordering = ['-enrolled_date']
        verbose_name_plural = 'Members'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def clean(self):
        # See overridden save().
        self.is_cleaned = True
        raise_message = 'The date must be in the future by at least one day.'
        if self.end_date <= (self.enrolled_date):
            raise ValidationError({'end_date': _(raise_message)})

    def save(self, *args, **kwargs):
        """
        Make sure clean() is called in case of calling individual save(), e.g.
        save instance from a shell.
        """
        # If clean() not called, call it and save().
        if self.is_cleaned is False:
            self.full_clean()
        super().save(*args, **kwargs)

    def get_remaining_days(self):
        """
        Return remaining days, as number, between enrolled date and end date.
        """
        try:
            return (self.end_date - self.enrolled_date).days
        except AttributeError as e:
            print(e)

    def get_gender(self):
        if self.gender == 'ml':
            return 'Male'
        elif self.gender == 'fl':
            return 'Female'
        else:
            return 'Unknown'
