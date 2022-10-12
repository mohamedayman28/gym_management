# Python
import datetime

from django.contrib.auth.models import User
# Django
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class Member(models.Model):
    MALE = 'ml'
    FEMALE = 'fl'
    GENDERS = [
        (MALE, 'Male'),
        (FEMALE, 'Female')
    ]

    # Relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    
    # Trigger for full_clean() in case of calling save() directly, for example using Django shell.
    is_cleaned = False

    def clean(self, *args, **kwargs):
        self.is_cleaned = True
        raise_message = 'The date must be in the future by at least one day.'
        if self.end_date <= (self.enrolled_date):
            raise ValidationError({'end_date': _(raise_message)})
        else:
            super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        """
        Clean fields in case of calling save() directly, for example using Django shell.
        """
        if self.is_cleaned is False:
            self.full_clean()
        else:
            super().save(*args, **kwargs)

    def get_remaining_days(self):
        """
        Return remaining days, as number, between self.enrolled_date and
        self.end_date.
        """
        try:
            return (self.end_date - self.enrolled_date).days
        except AttributeError as e:
            print(e)

    def get_gender_name(self):
        if self.gender == 'ml':
            return 'Male'
        elif self.gender == 'fl':
            return 'Female'
        else:
            return 'Unknown'
