
from django.contrib import admin

from Allmodels.models import Profile

# Register your models here.
@admin.register(Profile)
class CommentAdmin(admin.ModelAdmin):
    link_display_link = ("id","profile_user")
    