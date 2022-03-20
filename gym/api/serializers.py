# Local apps
from gym.models import Member
# Third party
from rest_framework import serializers


class MemberSerializer(serializers.ModelSerializer):
    member_id = serializers.IntegerField()

    class Meta:
        model = Member
        fields = ['member_id', 'user', 'first_name', 'last_name',
                  'gender', 'enrolled_date', 'end_date']
