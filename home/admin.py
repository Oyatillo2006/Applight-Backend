from django.contrib import admin

from .models import About, Features, Team, Test, Questions, Message

admin.site.register([About, Features, Team, Test, Questions, Message])
