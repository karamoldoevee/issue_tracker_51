from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile, Team


class ProfileInline(admin.StackedInline):
    model = Profile

    fields = ['birth_date', 'avatar', 'about_yourself', 'github_profile']


class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]

class TeamInline(admin.StackedInline):
    model = Team

    fields = ['user', 'project', 'work_started', 'work_finished']

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Team)

