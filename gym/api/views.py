# Local apps
from gym.api import serializers
from gym.models import Member
# Third party
from rest_framework import authentication, generics, permissions


class MemberListAPI(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class MemberCreateAPI(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class MemberDeleteAPI(generics.DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)


class MemberUpdateAPI(generics.UpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = serializers.MemberSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)
