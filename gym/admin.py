# Default django apps
from django.contrib import admin
# Local apps
from gym.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'remaining_days')

    def remaining_days(self, obj):
        return obj.get_remaining_days()  # pylint:disable=protected-access
