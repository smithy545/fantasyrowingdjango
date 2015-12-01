from django.contrib import admin

from .models import Team

class TeamAdmin(admin.ModelAdmin):
    fields = ["user", "name", "team_members"]
    filter_horizontal = ("team_members",)

admin.site.register(Team, TeamAdmin)
