# Default django apps
from django.contrib import admin
# Local apps
from gym.models import Member


admin.site.register(Member)
