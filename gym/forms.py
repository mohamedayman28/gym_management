# Django
from django import forms
# Local apps
from gym.models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['user', 'first_name', 'last_name',
                  'gender', 'enrolled_date', 'end_date']
